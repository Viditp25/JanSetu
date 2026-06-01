import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("cleaned_schemes.csv")

# Create database connection
conn = sqlite3.connect("schemes.db")

# Store table
df.to_sql("schemes", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()