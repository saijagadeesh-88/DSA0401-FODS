import pandas as pd

df = pd.read_csv("Q18.csv")

print(df['likes'].value_counts())