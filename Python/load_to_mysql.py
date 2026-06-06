import pandas as pd
from sqlalchemy import create_engine

# Read cleaned file
df = pd.read_csv("../Data/cleaned_superstore.csv")

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:ferrari458@127.0.0.1:3306/sales_dashboard"
)

# Upload
df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")
print("Rows:", len(df))