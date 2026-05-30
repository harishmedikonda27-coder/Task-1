import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# DATA CLEANING & VISUALIZATION PROJECT
# ==========================================

# Load dataset
df = pd.read_csv("D:/Retail_project/nvida_stock_prices.csv")

print("=" * 50)
print("DATA CLEANING & VISUALIZATION")
print("=" * 50)

# ==========================================
# 1. DATA UNDERSTANDING
# ==========================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# ==========================================
# 3. BASIC STATISTICS
# ==========================================

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# 4. VISUALIZATION
# ==========================================

# Closing Price Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'])

plt.title("NVIDIA Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# Trading Volume Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Volume'])

plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# Open vs Close Price
plt.figure(figsize=(8,5))
plt.scatter(df['Open'], df['Close'])

plt.title("Open Price vs Close Price")
plt.xlabel("Open Price")
plt.ylabel("Close Price")

plt.grid(True)

plt.show()

# High vs Low Price
plt.figure(figsize=(8,5))
plt.scatter(df['High'], df['Low'])

plt.title("High Price vs Low Price")
plt.xlabel("High Price")
plt.ylabel("Low Price")

plt.grid(True)

plt.show()

# ==========================================
# 5. CONCLUSION
# ==========================================

print("\nConclusion:")
print(
    "The dataset was cleaned by removing "
    "missing values and duplicates. "
    "Visualizations were created to understand "
    "stock price trends and trading behavior."
)