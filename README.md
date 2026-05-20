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
<img width="683" height="374" alt="Screenshot 2026-05-19 233912" src="https://github.com/user-attachments/assets/0f3568f7-9eef-488c-8e69-dce34242f85e" />


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

<img width="712" height="373" alt="Screenshot 2026-05-19 232438" src="https://github.com/user-attachments/assets/f96444a0-5e58-4181-a340-a2922a55ef02" />

