from cassandra.cluster import Cluster
import json

KEYSPACE = 'monitoring_events'
DB_FETCH_TIME_TAKEN_TABLE = 'db_fetch_itme_taken'


def create_session():
    cluster = Cluster()
    session = cluster.connect()
    return session


def shudown(cluster):
    cluster.shudown()


def create_keyspace_and_tables(session):
    create_keyspace_query = "CREATE KEYSPACE %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};" % KEYSPACE
    session.execute(create_keyspace_query)

    session.set_keyspace(KEYSPACE)

    create_table_query = "CREATE TABLE %s ( id uuid PRIMARY KEY, start_time float, time_taken float)" % DB_FETCH_TIME_TAKEN_TABLE
    session.execute(create_table_query)


def insert(session, data):
    insert_query = "INSERT INTO %s (id, start_time, time_taken) VALUES( %s, %s, %s);" % (
        DB_FETCH_TIME_TAKEN_TABLE, data['id'], data['start_time'], data['time_taken'])
    print(insert_query)
    session.execute(insert_query)


def get(session, id):
    get_query = "SELECT * FROM % WHERE id = " % (
        DB_FETCH_TIME_TAKEN_TABLE, id)


def store_event(session, event):
    data = json.loads(event)
    print("received event : ", data)
    insert(session, data)
