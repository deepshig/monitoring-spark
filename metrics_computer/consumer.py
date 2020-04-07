import pika
import time
import os
import sys
sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, consume  # NOQA
from metrics_computer.data_writer import create_session, create_keyspace_and_tables, store_event  # NOQA

init_queue()
db_session, db_cluster_shutdown = create_session()
create_keyspace_and_tables(db_session)


def msg_callback_handler(ch, method, properties, body):
    """function to receive the message from rabbitmq
    stores in cassandra DB
    ack the message"""

    event = body.decode('utf-8')
    store_event(db_session, event)
    # call the function to compute metrics
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)


try:
    consume(msg_callback_handler)
except:
    shutdown_queue()
    db_cluster_shutdown()
