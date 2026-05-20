import dlt

# customer Expectations
customer_rules = {
    "rule1":"customer_id IS NOT NULL",
    "rule2":"customer_name IS NOT NULL"
}
# ingesting the customer data
@dlt.table(
    name = "customer_stage"
)
@dlt.expect_all_or_drop(customer_rules)
def customer_stage():
  
  df = spark.readStream.table("my_catalog.source_schema.customers")
  return df