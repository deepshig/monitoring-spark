from pyspark import SparkContext
from pyspark.streaming import StreamingContext, DStream


def processor():
    sc = SparkContext(appName="MonitorinEvents_Streaming")
    sc.setLogLevel("WARN")

    ssc = StreamingContext(sc, 2)

    data = ssc.socketTextStream('0.0.0.0', 8080)
    data.pprint()

    ssc.start()
    ssc.awaitTermination()


processor()
