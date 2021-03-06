import sys
import json

sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, consume  # NOQA
from metrics_computer.data_writer import create_session, create_keyspace_and_tables, store_event  # NOQA
from metrics_computer.socket_client import create_socket  # NOQA

db_session = None
streaming_socket = None


def msg_callback_handler(ch, method, properties, body):
    """function to receive the message from rabbitmq
    stores in cassandra DB
    ack the message"""

    event = body.decode('utf-8')
    print("received event : {}".format(event))

    store_event(db_session, event)
    streaming_socket.sendall(str.encode(str(event) + "\n"))

    ch.basic_ack(delivery_tag=method.delivery_tag)


def init_consumer():
    init_queue()
    print("Initialised RabbitMQ")

    global db_session
    db_session, db_cluster_shutdown = create_session()
    create_keyspace_and_tables(db_session)
    print("Initialised Cassandra DB")

    global streaming_socket
    streaming_socket = create_socket()
    print("Created Streaming Socket")

    try:
        consume(msg_callback_handler)
    except Exception as e:
        print("callback handler failed {}".format(e))
        shutdown_queue()
        db_cluster_shutdown()
        streaming_socket.close()
