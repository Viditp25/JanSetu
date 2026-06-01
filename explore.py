import pandas as pd

df = pd.read_csv("archive/data/scheme.csv")

print(df.head())

print(df.columns)

print(df.info())