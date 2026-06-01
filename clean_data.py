import pandas as pd

# Load dataset
df = pd.read_csv("archive/data/scheme.csv")

# Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"])

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("cleaned_schemes.csv", index=False)

print(df.head())

print("Cleaned successfully!")