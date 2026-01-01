from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark cluster mode 2").getOrCreate()
    try:
        print(f"Spark version: {spark.version}")
        df = spark.createDataFrame([(1,)], ["column_name"])
        df.show()
    finally:
        spark.stop()