from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import json

KEYSPACE = 'monitoring_events'
DB_FETCH_TIME_TAKEN_TABLE = 'db_fetch_time_taken'


def create_session():
    cluster = Cluster(
        ['cassandra_node1', 'cassandra_node2', 'cassandra_node3'])
    session = cluster.connect()
    return session, cluster.shutdown


def create_keyspace_and_tables(session):
    create_keyspace_query = "CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 2};" % KEYSPACE
    session.execute(create_keyspace_query)

    session.set_keyspace(KEYSPACE)

    create_table_query = "CREATE TABLE IF NOT EXISTS %s ( id uuid PRIMARY KEY, start_time bigint, time_taken int, no_of_records int)" % DB_FETCH_TIME_TAKEN_TABLE
    session.execute(create_table_query)


def insert(session, data):
    insert_query = "INSERT INTO %s (id, start_time, time_taken, no_of_records) VALUES( %s, %s, %s, %s);" % (
        DB_FETCH_TIME_TAKEN_TABLE, data['id'], data['start_time'], data['time_taken'], data['no_of_records'])
    session.execute(insert_query)


def get(session, start_time):
    get_query = "SELECT * FROM %s WHERE start_time > %s ALLOW FILTERING; " % (
        DB_FETCH_TIME_TAKEN_TABLE, start_time)

    session.row_factory = dict_factory
    rows = session.execute(get_query)
    return rows


def store_event(session, event):
    data = json.loads(event)
    insert(session, data)
