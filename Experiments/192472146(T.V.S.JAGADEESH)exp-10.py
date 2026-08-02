import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q10 11.csv")

plt.plot(df['month'], df['sales'])
plt.title("Monthly Sales")
plt.show()