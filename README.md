# 📊 Retail Sales Analytics API

> End-to-End ETL + MySQL + FastAPI Backend for Retail Sales Analytics

------------------------------------------------------------------------

## 🚀 Overview

This project is a complete **Retail Sales Analytics Backend System**
built using:

-   **Pandas** → Data Cleaning & Transformation (ETL)
-   **MySQL** → Data Storage & Aggregation
-   **SQL Views** → Business Analytics Layer
-   **FastAPI** → REST API Backend
-   **Uvicorn** → ASGI Server

It processes raw retail transaction data and exposes customer and
product-level analytics through REST APIs.

------------------------------------------------------------------------

## 🏗 Architecture

    CSV Dataset
        ↓
    ETL Pipeline (Pandas)
        ↓
    MySQL Database (transactions table)
        ↓
    SQL Views (Aggregated Analytics)
        ↓
    FastAPI REST API
        ↓
    Swagger UI (/docs)

------------------------------------------------------------------------

## 📂 Project Structure

    Retail-Analytics-API/
    │
    ├── etl.py                # ETL Pipeline
    ├── main.py               # FastAPI Backend
    ├── requirements.txt      # Project Dependencies
    ├── .gitignore            # Ignored Files
    └── README.md             # Project Documentation

------------------------------------------------------------------------

## 🧹 ETL Pipeline Features

-   Invoice and StockCode normalization
-   Duplicate removal
-   Null value handling
-   Data type conversion
-   Date standardization
-   Revenue calculation (`TotalPrice`)
-   Bulk insert into MySQL
-   Primary key constraint handling

------------------------------------------------------------------------

## 🗄 Database Design

### 🧾 transactions Table

  Column        Description
  ------------- --------------------------------
  InvoiceNo     Invoice number
  StockCode     Product code
  Description   Product description
  Quantity      Units sold
  InvoiceDate   Transaction date
  UnitPrice     Price per unit
  CustomerID    Customer ID
  Country       Country
  TotalPrice    Revenue (Quantity × UnitPrice)

------------------------------------------------------------------------

## 📊 Analytical SQL Views

### 👤 customer_summary

Provides: - Total Orders - Total Items Purchased - Total Revenue Per
Customer

------------------------------------------------------------------------

### 📦 product_sales_overview

Provides: - Total Quantity Sold - Total Revenue Per Product

------------------------------------------------------------------------

## 🌐 API Endpoints

### 🔹 GET `/customer_summary`

Query Parameter:

    customer_id (optional)

Example:

    http://127.0.0.1:8000/customer_summary?customer_id=17850

------------------------------------------------------------------------

### 🔹 GET `/product_sales`

Query Parameter:

    product_code (optional)

Example:

    http://127.0.0.1:8000/product_sales?product_code=85123

------------------------------------------------------------------------

## 🛠 Installation & Setup

### 1️⃣ Clone Repository

    git clone https://github.com/yourusername/Retail-Analytics-API.git
    cd Retail-Analytics-API

------------------------------------------------------------------------

### 2️⃣ Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

### 3️⃣ Run ETL Pipeline

    python etl.py

------------------------------------------------------------------------

### 4️⃣ Create SQL Views

Run inside MySQL:

``` sql
USE testdb;

CREATE OR REPLACE VIEW customer_summary AS
SELECT 
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders,
    SUM(Quantity) AS TotalItems,
    SUM(Quantity * UnitPrice) AS TotalSpent
FROM transactions
GROUP BY CustomerID;

CREATE OR REPLACE VIEW product_sales_overview AS
SELECT 
    StockCode,
    SUM(Quantity) AS TotalSold,
    SUM(Quantity * UnitPrice) AS Revenue
FROM transactions
GROUP BY StockCode;
```

------------------------------------------------------------------------

### 5️⃣ Run FastAPI Server

    python -m uvicorn main:app --reload

Open Swagger UI:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 📈 Future Improvements

-   Pagination support
-   Date range filtering
-   Top customers endpoint
-   Authentication & JWT
-   Docker containerization
-   Cloud deployment
-   Environment variable configuration (.env)

------------------------------------------------------------------------

## 💼 Resume Description

> Developed an end-to-end Retail Sales Analytics backend using Pandas,
> MySQL, SQL Views, and FastAPI. Implemented ETL processing,
> business-level aggregations, and REST APIs for real-time analytics.

------------------------------------------------------------------------

## 🏆 Tech Stack

-   Python
-   Pandas
-   MySQL
-   FastAPI
-   Uvicorn

------------------------------------------------------------------------

## 📌 Author

**Raj Singh**
