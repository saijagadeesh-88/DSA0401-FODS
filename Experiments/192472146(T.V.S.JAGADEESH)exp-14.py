import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q14.csv")

plt.scatter(df['hours'], df['score'])
plt.show()