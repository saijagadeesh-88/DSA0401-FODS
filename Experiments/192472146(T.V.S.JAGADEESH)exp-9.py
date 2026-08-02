import pandas as pd

df = pd.read_csv("Q9.csv")

# Average price
print(df['price'].mean())

# Count per location
print(df['location'].value_counts())