from pyspark.sql import SparkSession
from os.path import basename

if __name__ == "__main__":
    filename = basename(__file__)
    print(filename)
    spark = SparkSession.builder.appName(filename).getOrCreate()
    try:
        print(f"Spark version: {spark.version}")
        df = spark.createDataFrame([(1,)], ["column_name"])
        df.show()
    finally:
        spark.stop()