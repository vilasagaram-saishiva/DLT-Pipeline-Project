import dlt

# product Expecation  
product_rules = {
    "rule1":"product_id IS NOT NULL",
    "rule2":"price >=0"
}
# ingesting the product 
@dlt.table(
    name = "products_stage"
)
@dlt.expect_all(product_rules)
def products_stage():
  
  df = spark.readStream.table("my_catalog.source_schema.products")
  return df

