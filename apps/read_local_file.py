"""
- You need to start a local master Spark session to read a file in the local filesystem.
- An alternative to this is upload the file to the HDFS or another object storage supported by PySpark like S3 or GCS, etc.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("Load file from local").getOrCreate()

try:
    df = spark.read.csv("file:///opt/spark/data/sample.csv", header=True, inferSchema=True)
    df.show()
finally:
    spark.stop()
