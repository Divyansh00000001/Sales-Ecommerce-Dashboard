import pandas as pd

# Load dataset
df = pd.read_csv(
    "../Data/Sample - Superstore.csv",
    encoding="latin1"
)

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create new columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()
df['Quarter'] = df['Order Date'].dt.quarter

# Profit Margin
df['Profit Margin %'] = round(
    (df['Profit'] / df['Sales']) * 100,
    2
)

# Replace infinite values
df.replace([float('inf'), -float('inf')], 0, inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

print("Final Shape:", df.shape)

# Save cleaned dataset
df.to_csv(
    "../Data/cleaned_superstore.csv",
    index=False
)

print("Cleaned dataset saved successfully!")