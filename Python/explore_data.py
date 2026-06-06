import pandas as pd

df = pd.read_csv(
    "../Data/Sample - Superstore.csv",
    encoding="latin1"
)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)