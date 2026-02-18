import pandas as pd
import mysql.connector
import re

def etl_pipeline(data_path):
    df = pd.read_csv(data_path, encoding='unicode_escape')

    def extract_numeric(value):
        match = re.search(r'\d+', str(value))
        return match.group(0) if match else None

    df['InvoiceNo'] = df['InvoiceNo'].apply(extract_numeric)
    df['StockCode'] = df['StockCode'].apply(extract_numeric)

    df.dropna(subset=['InvoiceNo', 'StockCode', 'CustomerID'], inplace=True)

    df['CustomerID'] = df['CustomerID'].astype(int)
    df['Quantity'] = df['Quantity'].astype(int)
    df['UnitPrice'] = df['UnitPrice'].astype(float)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df['InvoiceDate'] = df['InvoiceDate'].dt.strftime('%Y-%m-%d %H:%M:%S')

    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df


data_file = "online_retail.csv"
cleaned_df = etl_pipeline(data_file)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Krishnaseema"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
mycursor.execute("USE testdb")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    InvoiceNo VARCHAR(255),
    StockCode VARCHAR(255),
    Description TEXT,
    Quantity INT,
    Country VARCHAR(255),
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    InvoiceDate DATETIME,
    TotalPrice DECIMAL(10,2),
    PRIMARY KEY (InvoiceNo, StockCode, InvoiceDate)
)
""")

mydb.commit()

columns = ", ".join(cleaned_df.columns)
placeholders = ", ".join(["%s"] * len(cleaned_df.columns))

sql = f"INSERT IGNORE INTO transactions ({columns}) VALUES ({placeholders})"

mycursor.executemany(sql, cleaned_df.values.tolist())

mydb.commit()

print("ETL completed successfully!")

mycursor.close()
mydb.close()

