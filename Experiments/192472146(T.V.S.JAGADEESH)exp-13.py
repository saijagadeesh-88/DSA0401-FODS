# Question: Your task is to build a Python program that reads the stock data from a CSV file, calculates
# the variability of stock prices, and provides insights into the stock's price movements.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q13.csv")

plt.hist(df['price'])
plt.show()
