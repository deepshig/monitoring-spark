import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

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

results = spark.sql(
    "SELECT * FROM voting_records WHERE mx_missile='n' AND adoption_of_the_budget_resolution='n' AND religious_groups_in_schools='?'")
results.show()
