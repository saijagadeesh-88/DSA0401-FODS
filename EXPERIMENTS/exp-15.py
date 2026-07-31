import pandas as pd

# Sample data
data = {
    'City': ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Temperature': [32, 30, 28, 34, 29, 35]
}

df = pd.DataFrame(data)

# Mean temperature
mean_temp = df.groupby('City')['Temperature'].mean()

# Standard deviation
std_temp = df.groupby('City')['Temperature'].std()

# Temperature range
temp_range = df.groupby('City')['Temperature'].apply(lambda x: x.max() - x.min())

# Highest range city
highest_range_city = temp_range.idxmax()

# Most consistent city (lowest std)
consistent_city = std_temp.idxmin()

# Display
print("Mean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print("\nTemperature Range:\n", temp_range)
print("\nHighest Range City:", highest_range_city)
print("Most Consistent City:", consistent_city)