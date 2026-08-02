import pandas as pd

df = pd.read_csv("Q8.csv")

freq = df['product_name'].value_counts()

print(freq)