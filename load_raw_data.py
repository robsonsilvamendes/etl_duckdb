import duckdb
import os

def create_dir(folder='duckdb'):

    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"🚀 Folder '{folder}' successfully created.")
    else:
        print(f"✅ The Folder '{folder}' already exists.")

def load_data():
    # Connect to a persistent DuckDB file
    # If the file doesn't exist, this creates it
    con = duckdb.connect('./duckdb/ecommerce.duckdb')

    print("🚀 Starting ELT Process...")

    # 1. create a schema for raw data
    #con.sql("CREATE SCHEMA IF NOT EXISTS raw;")

    # 2. Load Sales Data (CSV)
    # read_csv_auto is a DuckDB magic function that infers types
    print("... Loading Sales Data")
    con.sql("""
        CREATE OR REPLACE TABLE ecommerece_sales_data_2024 AS 
        SELECT * FROM read_csv_auto('data/ecommerece_sales_data_2024.csv');
    """)

    # 3. Load Budget Data (CSV/Excel converted to CSV for simplicity)
    print("... Loading Budget Data")
    con.sql("""
        CREATE OR REPLACE TABLE product_details AS 
        SELECT * FROM read_csv_auto('data/product_details.csv');
    """)

    # 3. Load Budget Data (CSV/Excel converted to CSV for simplicity)
    print("... Loading Customes Details")
    con.sql("""
        CREATE OR REPLACE TABLE customer_details AS 
        SELECT * FROM read_csv_auto('data/customer_details.csv');
    """)
    
    # Validation check - to see if data is loaded into database successfully
    count = con.sql("SELECT count(*) FROM ecommerece_sales_data_2024").fetchone()
    print(f"✅ Loaded {count[0]} sales records.")
    
    con.close()

if __name__ == "__main__":
    create_dir()
    load_data()