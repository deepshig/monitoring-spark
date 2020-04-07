import pika
import os

QUEUE_NAME = 'monitoring_events'


def get_connection():
    amqp_url = os.environ['AMQP_URL']
    url_params = pika.URLParameters(amqp_url)

    connection = pika.BlockingConnection(url_params)
    return connection


def init_queue():
    connection = get_connection()
    chan = connection.channel()

    chan.queue_declare(queue=QUEUE_NAME, durable=True)


def shutdown_queue():
    connection = get_connection()
    chan = connection.channel()

    chan.close()
    connection.close()


def publish(message_body):
    connection = get_connection()
    chan = connection.channel()

    chan.basic_publish(exchange='', routing_key=QUEUE_NAME,
                       body=message_body, properties=pika.BasicProperties(delivery_mode=2))
    print("Produced the message")


def consume(callback_function):
    connection = get_connection()
    chan = connection.channel()

    chan.basic_qos(prefetch_count=1)
    chan.basic_consume(queue=QUEUE_NAME,
                       on_message_callback=callback_function)

    print("Waiting to consume")
    chan.start_consuming()
