from fastapi import FastAPI, HTTPException, Query
from typing import Optional
import mysql.connector

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Krishnaseema",
        database="testdb"
    )

@app.get("/customer_summary")
def get_customer_summary(customer_id: Optional[int] = None):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    if customer_id:
        cursor.execute("SELECT * FROM customer_summary WHERE CustomerID = %s", (customer_id,))
    else:
        cursor.execute("SELECT * FROM customer_summary LIMIT 100")

    data = cursor.fetchall()
    cursor.close()
    db.close()

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    return data


@app.get("/product_sales")
def get_product_sales(product_code: Optional[str] = None):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    if product_code:
        cursor.execute("SELECT * FROM product_sales_overview WHERE StockCode = %s", (product_code,))
    else:
        cursor.execute("SELECT * FROM product_sales_overview LIMIT 100")

    data = cursor.fetchall()
    cursor.close()
    db.close()

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    return data
