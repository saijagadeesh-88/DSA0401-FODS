import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q13.csv")

plt.hist(df['price'])
plt.show()