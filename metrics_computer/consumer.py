import socket
import threading
import time
import sys

sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, consume  # NOQA
from metrics_computer.data_writer import create_session, create_keyspace_and_tables, store_event  # NOQA
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

global db_session
global dispatcher

localhost = "localhost"
random_port = 9999


def msg_callback_handler(ch, method, properties, body):
    """function to receive the message from rabbitmq
    stores in cassandra DB
    ack the message"""
    time.sleep(1)
    event = body.decode('utf-8')
    print("body received : {}".format(event))
    try:
        # Store in cassandra
        store_event(db_session, event)
    except Exception as e:
        print("error storing entry in c* {}".format(e))
    # Send to Spark Streaming Context
    # call the function to compute metrics
    ch.basic_ack(delivery_tag=method.delivery_tag)
    try:
        print("dispatching event to socket")
        # global spark_socket
        # spark_socket.sendall(body)
        global dispatcher
        dispatcher(body)
        print("dispatch complete")
    except Exception as e:
        print("error sending to spark socket {}".format(e))


def open_socket():
    global conn
    try:
        # global spark_socket
        # spark_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # spark_socket.bind(('', random_port))
        print("spark_socket bound 1")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((localhost, random_port))
        s.listen(1)
        print("socket listening")
        conn, addr = s.accept()
        print("accept call complete")
        global dispatcher
        dispatcher = conn.sendall  # assigning sendall to dispatcher variable
        print("successfully created a socket")
    except Exception as e:
        print("unknown exception trying to bind socket {}".format(e))
        conn.close()


def processRdd(rdd):
    print("{}".format(rdd))


def spark_computation():
    sc = SparkContext(master="spark://spark-master:7077", appName="EntriesPerSecond")
    print("initialized spark connection!")
    ssc = StreamingContext(sc, 1)

    ssc.socketTextStream(localhost, random_port).countByWindow(1, 1).pprint(10)
    ssc.checkpoint("checkpointdir")
    ssc.start()
    print("initialized spark socket stream")
    ssc.awaitTermination()


def main():
    print("python main function")

    spark_host = "spark-master"
    spark_port = 7077

    init_queue()
    try:
        global db_session
        db_session, db_cluster_shutdown = create_session()
        create_keyspace_and_tables(db_session)
        print("initialized cassandra connection!")
    except Exception as e:
        print("error initializing cassandra connection {}".format(e))
    threading.Thread(target=open_socket).start()
    threading.Thread(target=spark_computation).start()

    try:
        consume(msg_callback_handler)
    except:
        shutdown_queue()
        db_cluster_shutdown()


if __name__ == '__main__':
    main()
