# val conf = new SparkConf()
# .setMaster("127.0.0.1:7077")
# .setAppName("congressional")
# .set("spark.streaming.receiver.writeAheadLog.enable",
#  "true")
#
# val ssc = new StreamingContext(conf,
#  Seconds(1))
# ssc.checkpoint(checkpointDirectory)
# //group by rows
# // in this case
# val events = ssc.socketTextStream(
# "localhost", 9999)
# .groupBy(e=>e(0))
# .countByKey()