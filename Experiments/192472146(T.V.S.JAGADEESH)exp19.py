# Question: Develop a Python program to calculate the frequency distribution of words in the customer
# reviews dataset?
import pandas as pd

df = pd.read_csv("Q19.csv")

text = " ".join(df['review'])

words = text.lower().split()

from collections import Counter
print(Counter(words))
