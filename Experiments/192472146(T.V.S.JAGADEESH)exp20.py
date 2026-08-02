import pandas as pd
from collections import Counter

df = pd.read_csv("Q20.csv")

text = " ".join(df['feedback'])

words = text.lower().split()

freq = Counter(words)

print(freq)