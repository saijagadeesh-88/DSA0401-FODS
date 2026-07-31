import pandas as pd

# Create sample stock data manually
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03',
             '2024-01-04', '2024-01-05'],
    'Close': [240, 250, 245, 260, 255]
}

df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate statistics
mean_price = df['Close'].mean()
std_dev = df['Close'].std()
max_price = df['Close'].max()
min_price = df['Close'].min()
range_price = max_price - min_price

# Display results
print("Mean Price:", mean_price)
print("Standard Deviation:", std_dev)
print("Price Range:", range_price)