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

# def processRdd(rdd):
#     print("{}".format(rdd))


# def spark_computation():
#     sc = SparkContext(master="spark://spark-master:7077",
#                       appName="EntriesPerSecond")
#     print("initialized spark connection!")
#     ssc = StreamingContext(sc, 1)

#     ssc.socketTextStream(localhost, random_port).countByWindow(1, 1).pprint(10)
#     ssc.checkpoint("checkpointdir")
#     ssc.start()
#     print("initialized spark socket stream")
#     ssc.awaitTermination()


def main():
    print("python main function")

    # spark_host = "spark-master"
    # spark_port = 7077

    init_queue()

    global db_session
    db_session, db_cluster_shutdown = create_session()
    create_keyspace_and_tables(db_session)

    global streaming_socket
    streaming_socket = create_socket()

    # threading.Thread(target=open_socket).start()
    # threading.Thread(target=spark_computation).start()

    try:
        consume(msg_callback_handler)
    except:
        shutdown_queue()
        db_cluster_shutdown()
        streaming_socket.close()


if __name__ == '__main__':
    main()
