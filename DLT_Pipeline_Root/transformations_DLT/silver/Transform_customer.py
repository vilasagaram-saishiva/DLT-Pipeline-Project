import dlt
from pyspark.sql.functions import col,upper


# Create Transformation View on customer data
@dlt.view(name="customer_enriched_view")
def customer_enriched_view():
    df = spark.readStream.table("customer_stage")
    df = df.withColumn("customer_name", upper(col("customer_name")))
    return df

# Create destination silver table of customer data
dlt.create_streaming_table(
    name="customer_enriched"
)

dlt.create_auto_cdc_flow(
    target="customer_enriched",
    source="customer_enriched_view",
    keys=["customer_id"],
    sequence_by=col("last_updated"),
    ignore_null_updates=False,
    stored_as_scd_type=1
)