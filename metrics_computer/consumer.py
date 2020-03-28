import pika
import time
import os
import sys
sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, consume  # NOQA
from metrics_computer.data_writer import create_session, create_keyspace_and_tables, store_event, shudown  # NOQA

init_queue()
db_session = create_session()
create_keyspace_and_tables(db_session)


def msg_callback_handler(ch, method, properties, body):
    """function to receive the message from rabbitmq
    print it
    sleep for 2 seconds
    ack the message"""

    event = body.decode('utf-8')
    store_event(db_session, event)
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)


consume(msg_callback_handler)
shutdown_queue()
