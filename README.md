# Real-Time-Heath-Monitoring-System
Real-time health data ingestion and visualization pipeline using Azure Data Factory, SSIS, SQL Server, and Power BI. Tracks COVID trends, computes KPIs, and displays insights in a dynamic dashboard.

## 🚀 Technologies Used
- Azure Data Factory
- SQL Server & SSIS
- Python (requests, pandas)
- Power BI
- GitHub
- REST API (disease.sh)

## 🔁 Pipeline Overview
- Extract: API call to fetch daily COVID-19 stats.
- Transform: Calculates recovery and mortality rates.
- Load: Transformed data pushed to Azure SQL via ADF/SSIS.
- Visualize: Power BI dashboard connects to SQL for real-time trends.

## 📂 Project Structure

real-time-health-dashboard/
├── data_pipeline/          # ADF & SSIS ETL pipeline files
├── dashboard/              # Power BI visuals and docs
├── scripts/                # Python scripts for ingestion and transformation
├── notebooks/              # EDA and forecasting (optional)
├── assets/                 # Architecture diagrams
├── README.md               # Project documentation

---

## ✅ Features
- Real-time data ingestion
- Reusable ETL design (Python → ADF/SSIS → SQL Server)
- Visual KPIs and trends by date/country


## 📦 Setup

```bash
pip install -r requirements.txt
python scripts/fetch_api_data.py
python scripts/transform_data.py
```

## 📜 License
MIT License
