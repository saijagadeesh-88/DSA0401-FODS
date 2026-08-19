# Question: Using Pandas DataFrame operations, how would you find the following information from
# the property_data DataFrame:
# 1. The average listing price of properties in each location.
# 2. The number of properties with more than four bedrooms.
# 3. The property with the largest area.
import pandas as pd

df = pd.read_csv("Q9.csv")

# Average price
print(df['price'].mean())

# Count per location
print(df['location'].value_counts())
