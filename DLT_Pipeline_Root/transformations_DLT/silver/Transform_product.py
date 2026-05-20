import dlt
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

# Create Transformation View on Product
@dlt.view(name="products_enriched_view")
def products_enriched_view():
    df = spark.readStream.table("products_stage")
    df = df.withColumn("price", col("price").cast(IntegerType()))
    return df

# Create destination silver table of products
dlt.create_streaming_table(
    name="products_enriched"
)

dlt.create_auto_cdc_flow(
    target="products_enriched",
    source="products_enriched_view",
    keys=["product_id"],
    sequence_by=col("last_updated"),
    ignore_null_updates=False,
    stored_as_scd_type=1
)