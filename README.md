# 🛒 Retail Sales Analytics API

## 📌 Overview

This project implements a complete **ETL (Extract, Transform, Load)
pipeline** using Python, Pandas, and MySQL to process retail transaction
data.

After cleaning and structuring the data, a **FastAPI backend
application** exposes RESTful APIs to retrieve:

-   Customer-level sales summaries
-   Product-level sales insights

The system demonstrates end-to-end backend engineering including data
processing, database modeling, SQL aggregation, and API development.

------------------------------------------------------------------------

## 🚀 Features

### 🔹 ETL Pipeline

-   Cleans raw CSV transaction data
-   Handles null values and duplicates
-   Normalizes invoice & product codes
-   Converts and standardizes date formats
-   Calculates revenue (`TotalPrice = Quantity × UnitPrice`)
-   Bulk inserts cleaned data into MySQL

### 🔹 MySQL Database

-   Structured `transactions` table
-   Optimized schema design
-   SQL Views for business-level analytics

### 🔹 FastAPI Application

-   RESTful API endpoints
-   Query-based filtering
-   Swagger UI documentation
-   Real-time database querying

------------------------------------------------------------------------

## 🏗 Project Architecture

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
    ├── etl.py                # ETL Pipeline Script
    ├── main.py               # FastAPI Backend
    ├── requirements.txt      # Project Dependencies
    ├── .gitignore            # Ignored Files
    └── README.md             # Project Documentation

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

Ensure the following are installed:

-   Python 3.12+
-   MySQL Server
-   MySQL Workbench (optional but recommended)
-   Dataset in CSV format

------------------------------------------------------------------------

### 2️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 3️⃣ MySQL Setup

``` sql
CREATE DATABASE retaildb;
USE retaildb;
```

> Note: The ETL script can be configured to create tables automatically.

------------------------------------------------------------------------

### 4️⃣ Run ETL Pipeline

``` bash
python etl.py
```

------------------------------------------------------------------------

### 5️⃣ Create Analytical SQL Views

``` sql
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

### 6️⃣ Run FastAPI Server

``` bash
uvicorn main:app --reload
```

------------------------------------------------------------------------

## 🌐 API Documentation

-   Swagger UI → http://127.0.0.1:8000/docs
-   ReDoc → http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

## 📊 API Endpoints

### 1️⃣ Get Customer Summary

**Endpoint:** `GET /customer_summary`\
**Query Parameter:** `customer_id` (optional, integer)

Example:

    GET http://127.0.0.1:8000/customer_summary?customer_id=17850

Sample Response:
 ```json
[
    {
    "CustomerID": 17850,
    "TotalOrders": 35,
    "TotalItems": 1607,
    "TotalSpent": 4996.37,
    }
]
 ```

------------------------------------------------------------------------

### 2️⃣ Get Product Sales Overview

**Endpoint:** `GET /product_sales`\
**Query Parameter:** `product_code` (optional, string)

Example:

    GET http://127.0.0.1:8000/product_sales?product_code=85123

Sample Response:
```json
[
  {
    "StockCode": "85123",
    "TotalSold": 34068,
    "Revenue": 93578,
  }
]
```
------------------------------------------------------------------------

## 🧪 Sample Queries

Retrieve all customers:
```sh
GET /customer_summary
```

Retrieve specific customer:
```sh
GET /customer_summary?customer_id=12345
```

Retrieve all products:
```sh
GET /product_sales
```

Retrieve specific product:
```sh
GET /product_sales?product_code=85123
```

------------------------------------------------------------------------

## 🔐 Database Configuration

Modify credentials in your script:

``` python
DB_HOST = "127.0.0.1"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "retaildb"
```

------------------------------------------------------------------------

## 📈 Future Improvements

-   Pagination support
-   Date range filtering
-   Top customers endpoint
-   JWT Authentication
-   Docker containerization
-   Environment variable configuration (.env)
-   Cloud deployment

------------------------------------------------------------------------

## 💼 Resume Description

Developed an end-to-end Retail Sales Analytics backend system using
Pandas, MySQL, SQL Views, and FastAPI. Implemented data cleaning,
transformation pipelines, business-level aggregations, and REST APIs for
real-time analytics reporting.

------------------------------------------------------------------------

## 🏆 Tech Stack

-   Python
-   Pandas
-   MySQL
-   FastAPI
-   Uvicorn

------------------------------------------------------------------------

## 👨‍💻 Author

Raj Singh
