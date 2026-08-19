# Question:
# 1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened in a
# month?
# 2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a month?
# 3. Develop a Python program to create a bar plot of the monthly sales data.
# import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q10 11.csv")

plt.bar(df['month'], df['sales'])
plt.title("Bar Chart")
plt.show()
