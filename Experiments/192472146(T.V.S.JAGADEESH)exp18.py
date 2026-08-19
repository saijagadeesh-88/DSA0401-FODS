# Question: Develop a Python program to calculate the frequency distribution of likes among the posts?
import pandas as pd

df = pd.read_csv("Q18.csv")

print(df['likes'].value_counts())
