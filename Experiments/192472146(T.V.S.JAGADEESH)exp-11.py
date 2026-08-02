import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q10 11.csv")

plt.bar(df['month'], df['sales'])
plt.title("Bar Chart")
plt.show()