import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def processor():
    sc = SparkContext(appName="MonitorinEvents_Streaming")
    sc.setLogLevel("WARN")

    batch_duration = 1
    window_duration = 10
    slide_duration = 5

    ssc = StreamingContext(sc, batch_duration)
    ssc.checkpoint("checkpointdir")
    print("creating spark streaming context")

    data_stream = ssc.socketTextStream('0.0.0.0', 8080)

    # Print the number of records in 10 second window - print once every 5 second
    data_stream.countByWindow(window_duration, slide_duration).pprint()

    # Print the Time taken moving average - print once every 5s for a window of past 10s
    # data_stream.map(tojson).reduceByKeyAndWindow(lambda x, y: (x["time_taken"] + y["time_taken"])/2, lambda x, y: (x["time_taken"] - y["time_taken"])/2, window_duration, slide_duration).pprint()
    # data_stream.reduceByKeyAndWindow()
    # data = data_stream.map(lambda x: "Val : " + x).pprint()

    print("starting spark socket connection")
    ssc.start()
    ssc.awaitTermination()


# def print_rdd_count(rdd):
#     count = 0
#     for row in rdd.collect():
#         print(row)
#         count = count + 1
#     print("rdd {} count: {} <- vals -> {}".format(rdd, rdd.count(), count))


# def tojson(input):
#     output = json.loads(input)
#     print(output)
#     return output
