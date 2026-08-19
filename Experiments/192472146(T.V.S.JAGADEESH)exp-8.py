# Question: How would you find the top 5 products that have been sold the most in the past month?
import pandas as pd

df = pd.read_csv("Q8.csv")

freq = df['product_name'].value_counts()

print(freq)
