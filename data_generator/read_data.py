from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import SparkSession
from pyspark import SparkContext
import pyspark
import time
import uuid
import json
import sys
sys.path.append('../')

from rabbitmq.manager import init_queue, shutdown_queue, publish  # NOQA
from query import generate_query  # NOQA

sc = SparkContext()

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("class_name", StringType()),
    StructField("handicapped_infants", StringType()),
    StructField("water_project_cost_sharing", StringType()),
    StructField("adoption_of_the_budget_resolution", StringType()),
    StructField("physician_fee_freeze", StringType()),
    StructField("el_salvador_aid", StringType()),
    StructField("religious_groups_in_schools", StringType()),
    StructField("anti_satellite_test_ban", StringType()),
    StructField("aid_to_nicaraguan_contras", StringType()),
    StructField("mx_missile", StringType()),
    StructField("immigration", StringType()),
    StructField("synfuels_corporation_cutback", StringType()),
    StructField("education_spending", StringType()),
    StructField("superfund_right_to_sue", StringType()),
    StructField("crime", StringType()),
    StructField("duty_free_exports", StringType()),
    StructField("export_administration_act_south_africa", StringType())
])

print()

data = spark.read.csv("./sample_data.csv", header=True, schema=schema)
data.registerTempTable("voting_records")


def publish_metric(start_time, end_time):
    time_taken = end_time - start_time
    event = {
        "id": str(uuid.uuid4()),
        "start_time": start_time,
        "time_taken": time_taken
    }

    event_json = json.dumps(event)
    publish(event_json)


init_queue()

for i in range(1000000):
    start_time = time.time()

    select_query = generate_query()
    print(select_query)
    results = spark.sql(select_query)

    end_time = time.time()
    results.show()

    publish_metric(start_time, end_time)

shutdown_queue()
