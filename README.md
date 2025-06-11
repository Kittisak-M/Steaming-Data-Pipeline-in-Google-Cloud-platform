# 👗 Streaming Data Pipeline in Google Cloud Platform

## 📌 Business Purpose

Fastyle is a rapidly expanding fast-fashion company with **20 branches nationwide**. As the business grows, efficiently managing inventory and analyzing sales data is critical for sustainable growth and profitability. Fastyle also plans to expand into online sales, making centralized and accessible data even more essential.

Currently, data is scattered across systems, making it hard for the data team to extract insights. This project aims to build a **scalable, real-time data engineering pipeline** to support business growth and improve data accessibility.

### ✅ Project Scope Includes:
- ETL/ELT pipeline development  
- Cost estimation and cloud optimization  
- Real-time streaming architecture  
- Creation of a data mart for reporting
- Deploy API
---

## 🗂️ Data Sources
(*To be defined – e.g., POS systems, inventory databases, e-commerce platforms.*)

---

## 🧰 Data Stack

- **Pub/Sub** – Real-time data ingestion (e.g., sales transactions, inventory changes)  
- **Cloud Storage** – Raw data lake storage  
- **Cloud Composer (Apache Airflow)** – Orchestration of ETL pipelines
- **Cloud SQL**
- **BigQuery** – Scalable data warehouse for analytics and reporting  

---

## 🎯 Business Goals

### 1. Inventory Management Optimization  
- Implement a reliable streaming pipeline to track inventory across the central warehouse and 20 retail branches  
- Enable real-time inventory visibility to prevent stockouts and overstock situations  
- Improve supply chain efficiency and customer satisfaction

### 2. Sales Performance Reporting  
- Build data models to calculate **Gross Merchandise Value (GMV)** segmented by:
  - Customer type (e.g., new vs. returning)  
  - Product category (e.g., tops, bottoms, accessories)  
- Provide marketing and sales teams with insights for targeted campaigns and product strategies

### 3. Profitability Analysis  
- Generate reports showing **gross profit margin by product category**  
- Support data-driven decisions in pricing, promotions, and inventory planning  
- Maximize business profitability using reliable metrics

---

## 🚀 Outcome

A cloud-native, cost-optimized, and scalable data pipeline that supports real-time analytics, inventory visibility, and business intelligence reporting.

---

## 📅 Next Steps

- [ ] Define and integrate data sources  
- [ ] Set up Pub/Sub topics for streaming ingestion  
- [ ] Design data models in BigQuery  
- [ ] Schedule Airflow DAGs for transformation workflows  
- [ ] Build dashboards for inventory and sales reporting  

---

## 📫 Contact

For more details, feel free to reach out at [your-email@example.com]
