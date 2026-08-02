import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q12.csv")

plt.scatter(df['temperature'], df['rainfall'])
plt.show()