import sqlite3
import pandas as pd

conn = sqlite3.connect("schemes.db")

query = """
SELECT scheme_name, category
FROM schemes
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()

print("Query executed successfully!")
