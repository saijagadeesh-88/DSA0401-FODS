# Question: Create a Python program that fulfills these requirements and helps your team gain insights
# from the customer feedback data.
import pandas as pd
from collections import Counter

df = pd.read_csv("Q20.csv")

text = " ".join(df['feedback'])

words = text.lower().split()

freq = Counter(words)

print(freq)
