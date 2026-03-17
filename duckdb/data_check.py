import duckdb

con = duckdb.connect('./duckdb/ecommerce.duckdb')
# Querying the dbt model (which is now a table/view in the DB)
df = con.sql("SELECT * FROM marts.sales").df()
print(df)