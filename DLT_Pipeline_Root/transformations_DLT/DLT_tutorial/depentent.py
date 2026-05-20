# from pyspark import pipelines as dp
# from pyspark.sql.functions import *

# """ Creating an End to End Pipeline"""

# #staging materialized View to read the data
# @dp.table(
#     name = "staging_orders" 
# )
# def staging_orders():
#     df = spark.read.table("my_catalog.source_schema.orders")
#     return df

# #Transfromation 
# @dp.table(
#     name = "Transformation_orders" 
# )
# def Transformation_orders():
#     df = spark.readStream.table("staging_orders")
#     df = df.withColumn("order_status",upper(col("order_status")))
#     return df

# #Aggregated View 
# @dp.table(
#     name = "Aggregated_orders" 
# )
# def Aggregated_orders():
#     df = spark.readStream.table("Transformation_orders")
#     df = df.groupBy("order_status").count()
#     return df
