import pandas as pd

df = pd.read_csv("Q17.csv")

print(df['age'].value_counts())