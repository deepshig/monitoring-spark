import pika
import time
import os

QUEUE_NAME: 'monitoring_events'


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


def receive_msg(ch, method, properties, body):
    """function to receive the message from rabbitmq
    print it
    sleep for 2 seconds
    ack the message"""

    print('received msg : ', body.decode('utf-8'))
    time.sleep(2)
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume():
    connection = get_connection()
    chan = connection.channel()

    chan.basic_qos(prefetch_count=1)
    chan.basic_consume(queue='hello',
                       on_message_callback=receive_msg)

    print("Waiting to consume")
    chan.start_consuming()
