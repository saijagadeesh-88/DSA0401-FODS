# Question: Using NumPy arrays and operations, how would you find the average sale price of houses
# with more than four bedrooms in the neighborhood?
import pandas as pd

df = pd.read_csv("Q3.csv")

print(df)

# Basic statistics
print(df.describe())
