import dlt
from pyspark.sql.functions import col

# Create Transformation View
@dlt.view(name="sales_enriched_view")
def sales_enriched_view():
    df = spark.readStream.table("sales_stage")
    df = df.withColumn("total_amount", col("quantity") * col("amount"))
    return df

# Create destination silver table
dlt.create_streaming_table(
    name="sale_enriched"
)

dlt.create_auto_cdc_flow(
    target="sale_enriched",
    source="sales_enriched_view",
    keys=["sales_id"],          # change to sale_id if your column is actually sale_id
    sequence_by=col("sale_timestamp"),
    ignore_null_updates=False,
    stored_as_scd_type=1
)