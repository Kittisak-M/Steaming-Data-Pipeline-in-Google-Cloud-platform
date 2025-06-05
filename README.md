# 🛒 TrendMart E-Commerce Data Platform (GCP Practice Project)

## 📌 Overview
This project simulates a real-world data engineering scenario for an e-commerce company, **TrendMart**, aiming to build a modern analytics platform on **Google Cloud Platform (GCP)**. It covers ingestion, processing, storage, and visualization using GCP-native tools.

---

## 🎯 Business Objective
TrendMart wants to centralize its data to enable:

- Real-time and batch analytics
- Customer 360° views
- Daily sales & marketing performance dashboards
- Real-time product trend monitoring

---

## 📂 Data Sources

| Source                   | Type       | Description                                      | Frequency  |
|--------------------------|------------|--------------------------------------------------|------------|
| Website Clickstream      | Streaming  | Page views, add-to-cart, purchases               | Real-time  |
| Sales Transactions       | Batch      | Orders from country-specific databases           | Daily      |
| Marketing Campaigns      | Batch (CSV)| Data from Meta Ads & Google Ads                  | Daily      |
| Customer Support Tickets | API        | Tickets from Zendesk                             | Hourly     |

---

## 🧰 Tools & Technologies (GCP)

| Layer             | Tool                  |
|-------------------|------------------------|
| Ingestion         | Pub/Sub, Cloud Storage, Cloud Functions |
| Processing        | Dataflow (Apache Beam), Dataproc (Spark) |
| Storage (Raw)     | Cloud Storage         |
| Warehouse         | BigQuery              |
| Orchestration     | Cloud Composer (Airflow) |
| Visualization     | Looker / Looker Studio |
| Access Control    | IAM                    |

---

## 🛠 Functional Requirements

- Ingest real-time website event data via **Pub/Sub**.
- Load daily batch CSV files from marketing and sales to **Cloud Storage**.
- Use **Cloud Functions** to trigger ETL jobs upon file arrival.
- Use **Dataflow or Dataproc** for data cleaning and transformation.
- Load cleaned data into **BigQuery** as the central data warehouse.
- Schedule pipelines with **Cloud Composer (Airflow)**.
- Visualize KPIs with **Looker Studio** or **Looker**.

---

## 🎯 Key KPIs & Outputs

- 📈 Sales trends (daily/weekly/monthly)
- 💰 Conversion rates by channel
- 👤 Customer retention & lifetime value
- 🔝 Top-selling products
- 🚨 Real-time alerts for product view/sales spikes
- 📊 Data APIs for internal use

---

## 🔒 Data Governance

- Store **raw data** for 1 year (cold storage).
- Store **processed data** for 6 months (hot storage).
- **Mask PII** such as customer emails and phone numbers.
- Apply **role-based access control** via IAM.

---

## 📌 Your Practice Tasks

1. **Design a GCP Architecture Diagram**
2. **Mock data pipeline**:
   - CSV → Cloud Storage → Dataflow → BigQuery
3. **Write SQL queries** in BigQuery for KPI reporting
4. (Optional) Deploy **Airflow DAG** in Cloud Composer
5. (Optional) Build dashboards in Looker Studio

---

## 📁 Project Structure (Suggested)

