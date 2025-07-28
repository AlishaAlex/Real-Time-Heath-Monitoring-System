# 📌 ETL Pipeline Documentation

## 🔄 Overview
This ETL process fetches COVID-19 data from a public API, transforms it to calculate recovery and mortality rates, and loads it into an Azure SQL Database using either Azure Data Factory or SSIS.

## 🧱 Components
- **Extract:**
  - `fetch_api_data.py` script retrieves data from https://disease.sh API and saves it to `covid_data_raw.csv`.

- **Transform:**
  - `transform_data.py` computes `recovery_rate` and `mortality_rate` fields.
  - Output saved to `covid_data_transformed.csv`.

- **Load:**
  - **Azure Data Factory:**
    - Dataset: DelimitedText for input, Azure SQL for output.
    - Pipeline: Copy Activity scheduled every 15 minutes.
    - Linked Services: Azure Blob Storage and Azure SQL Database.

  - **SSIS (Alternative):**
    - Use Flat File Source → Derived Column Transformation → OLE DB Destination.

## 🔁 Refresh Frequency
Every 15 minutes using a scheduler (Python loop, cron job, or Azure Data Factory triggers).

## 🛠️ Error Handling
- API failures raise exceptions.
- CSV read/write includes basic validation.
- ADF pipeline uses failure alerts.
