# Question: Identify any potential correlation between study time and exam scores and explore various
# plotting functions to visualize this relationship effectively.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q14.csv")

plt.scatter(df['hours'], df['score'])
plt.show()
