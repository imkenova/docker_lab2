from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg


spark = SparkSession.builder.appName("HousePrices") \
    .config("spark.driver.extraClassPath", "/opt/bitnami/spark/jars/postgresql-42.7.0.jar") \
    .getOrCreate()

jdbc_url = "jdbc:postgresql://postgres:5432/db_spark_app"
connection_properties = {
    "user": "user",
    "password": "pass123",
    "driver": "org.postgresql.Driver"
}

house_prices_df = spark.read \
    .jdbc(url=jdbc_url, table="house_prices", properties=connection_properties)

result_df = house_prices_df.groupBy("location", "bedrooms").agg(avg("price").alias("avg_price")) \
    .orderBy("location", "bedrooms")

result_df.show()

spark.stop()
