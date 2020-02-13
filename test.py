import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pandas as pd

sc = SparkContext()

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("ID", IntegerType()),
    StructField("Country", StringType()),
    StructField("Capital", StringType())
])

print()

data = spark.read.csv("./data.csv", header=True, schema=schema)
data.show()
data.registerTempTable("countries")

results = spark.sql("SELECT Capital FROM countries WHERE ID=3")
results.show()
