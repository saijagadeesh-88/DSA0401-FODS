# Question:
# 1. Develop a Python program to create a line plot of the monthly temperature data.
# 2: Develop a Python program to create a scatter plot of the monthly rainfall data.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q12.csv")

plt.scatter(df['temperature'], df['rainfall'])
plt.show()
