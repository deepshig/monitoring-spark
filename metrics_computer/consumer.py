from pyspark.streaming import StreamingContext
from pyspark import SparkContext
import socket
import threading
import time
import sys

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

    store_event(db_session, event)
    streaming_socket.sendall(str.encode(event))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    print("python main function")

    init_queue()

    global db_session
    db_session, db_cluster_shutdown = create_session()
    create_keyspace_and_tables(db_session)

    global streaming_socket
    streaming_socket = create_socket()

    try:
        consume(msg_callback_handler)
    except:
        shutdown_queue()
        db_cluster_shutdown()
        streaming_socket.close()


if __name__ == '__main__':
    main()
