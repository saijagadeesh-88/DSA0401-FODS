# Question:
# 1. How would you develop a Python program to create a line plot of the monthly sales data?
# 2: How would you develop a Python program to create a bar plot of the monthly sales data?
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q10 11.csv")

plt.plot(df['month'], df['sales'])
plt.title("Monthly Sales")
plt.show()
