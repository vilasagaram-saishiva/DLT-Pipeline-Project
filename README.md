# Delta Live Tables (DLT) End-to-End Data Engineering Project

## Project Overview

This project demonstrates an end-to-end Medallion Architecture implementation using Databricks Delta Live Tables (DLT).

The pipeline ingests streaming customer, product, and sales data into Bronze tables, performs cleansing and CDC handling in Silver tables, and finally builds Gold-level dimensional and business aggregation tables for analytics.

The implementation includes:

- Streaming ingestion
- Data quality expectations
- CDC (Change Data Capture)
- SCD Type 1 & Type 2
- Materialized tables
- DLT Views
- Incremental processing
- Business aggregation layer

---

# Architecture

Source Tables
    ↓
Bronze Layer (Raw Streaming Ingestion + Expectations)
    ↓
Silver Layer (Transformations + CDC + Cleansing)
    ↓
Gold Layer (Fact/Dimension Modeling + Business Aggregations)

---

# Project Structure

```text
DLT_Pipeline_Root/
│
├── explorations/
│
├── transformations_DLT/
│
│   ├── bronze/
│   │   ├── customers_ingestion.py
│   │   ├── product_ingestion.py
│   │   └── sale_ingestion.py
│   │
│   ├── silver/
│   │   ├── Transform_customer.py
│   │   ├── Transform_product.py
│   │   └── Transform_sales.py
│   │
│   └── gold/
│       ├── dim_customer.py
│       ├── dim_product.py
│       ├── fact_sales.py
│       └── business_sales.py
│
└── README.md


