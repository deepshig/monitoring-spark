import pandas as pd
from statistics import median, stdev
import sys
import datetime
import time
sys.path.append('../')

from metrics_computer.data_writer import create_session, create_keyspace_and_tables, get  # NOQA


def fetch_data(db_session):
    current_time = datetime.datetime.now()

    query_time = current_time - datetime.timedelta(seconds=5)
    query_time_epoch = int(query_time.timestamp() * 1000)

    rows = get(db_session, query_time_epoch)

    return rows


def process_data(rows):
    time_taken_list = []
    for row in rows:
        time_taken = row['time_taken']
        time_taken_list.append(time_taken)

    if len(time_taken_list) > 1:
        print("Median : ", median(time_taken_list))
        print("Standard Deviation : ", stdev(time_taken_list))
        print("++++++++++++")


def batch_processor():
    db_session, db_cluster_shutdown = create_session()
    create_keyspace_and_tables(db_session)
    print("Batch Processor : Initialised Cassandra DB")

    while True:
        time.sleep(3)
        rows = fetch_data(db_session)
        process_data(rows)
