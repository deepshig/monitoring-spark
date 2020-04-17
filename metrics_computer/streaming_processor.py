from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def processor():
    sc = SparkContext(appName="MonitorinEvents_Streaming")
    sc.setLogLevel("WARN")

    ssc = StreamingContext(sc, 1)

    data_stream = ssc.socketTextStream('0.0.0.0', 8080)
    data = data_stream.map(lambda x: "Val : " + x).pprint()

    ssc.start()
    ssc.awaitTermination()


processor()
