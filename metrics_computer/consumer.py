import pika
import time
import os
import sys
sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, consume  # NOQA


def msg_callback_handler(ch, method, properties, body):
    """function to receive the message from rabbitmq
    print it
    sleep for 2 seconds
    ack the message"""

    print('received msg : ', body.decode('utf-8'))
    time.sleep(2)
    print('acking it')
    ch.basic_ack(delivery_tag=method.delivery_tag)


init_queue()
consume(msg_callback_handler)
shutdown_queue()
