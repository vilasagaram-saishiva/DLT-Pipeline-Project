# from pyspark import pipelines as dp

# # Stream Table creatation

# @dp.table(
#     name = "orders_stream_table"
# )
# def orders_stream_table():
#     """
#     Reads the Table in the specified directory 
#     """
#     df = spark.readStream.table("my_catalog.source_schema.orders")
#     return  df

# # Batch table on the same order table

# @dp.table(
#     name = "orders_Materialized_table"
# )
# def orders_Materialized_table():
#     """
#     Reads the Table in the specified directory 
#     """
#     df = spark.read.table("my_catalog.source_schema.orders")
#     return  df

# # Streaming View
# @dp.view(
#     name = "orders_stream_view"
# )
# def orders_stream_view():
#     """
#     Reads the Table in the specified directory 
#     """
#     df = spark.readStream.table("my_catalog.source_schema.orders")
#     return  df

# # batch view

# @dp.view(
#     name = "orders_Materialized_view"
# )
# def orders_Materialized_view():
#     """
#     Reads the Table in the specified directory 
#     """
#     df = spark.read.table("my_catalog.source_schema.orders")
#     return  df