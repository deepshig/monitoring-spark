import json
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def processor():
    sc = SparkContext(appName="MonitoringEvents_Streaming")
    sc.setLogLevel("WARN")

    batch_duration = 1
    window_duration = 10
    slide_duration = 5

    ssc = StreamingContext(sc, batch_duration)
    ssc.checkpoint("checkpointdir")

    data_stream = ssc.socketTextStream('0.0.0.0', 8080)

    # Print the number of records in 10 second window - print once every 5 second
    data_stream.countByWindow(window_duration, slide_duration).pprint()

    ssc.start()
    ssc.awaitTermination()
