# Data-Project-1

**Project Overview:** Built an end-to-end data pipeline utilizing **Excel** for data discovery, **Python (Pandas)** for automated ETL operations, and **SQL** for deep analytical querying.

### Technical Stack Used
* **Data Validation, Collection, Inspection:** Microsoft Excel
* **ETL & Data Engineering:** Python (Pandas)
* **Data Warehousing & Analytics:** Google BigQuery (SQL)
* **Business Intelligence:** Power BI

### ⚙️ Pipeline Architecture
1. **Extraction (Excel):** Evaluated raw data schemas across disconnected traffic logs and e-commerce transactional files.
2. **Transformation (Python):** Automated data cleansing via a custom Pandas script to programmatically resolve missing values and execute an optimized data-merge -- mapping traffic timestamps to conversions.
3. **Analysis (SQL):** Ingested the production-ready dataset into BigQuery to calculate metrics including conditional order frequencies, conversion percentages, and Average Order Value.