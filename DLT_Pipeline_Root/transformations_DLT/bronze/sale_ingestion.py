import dlt

# sales Expecation  
sales_rules = {
    "rule1":"sales_id IS NOT NULL"
}

# Empty Streaming Table
dlt.create_streaming_table(
    name = "sales_stage",
    expect_all_or_drop = sales_rules
)

# Create East Sales Flow
@dlt.append_flow(target = "sales_stage")
def east_sales():

    df = spark.readStream.table("my_catalog.source_schema.sales_east")
    return df
# Create West Sales Flow
@dlt.append_flow(target = "sales_stage")
def west_sales():

    df = spark.readStream.table("my_catalog.source_schema.sales_west")
    return df