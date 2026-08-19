# Question: Develop a code in python to find the frequency distribution of the ages of the customers who
# have made a purchase in the past month.
import pandas as pd

df = pd.read_csv("Q17.csv")

print(df['age'].value_counts())
