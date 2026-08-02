import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q15.csv")

for city in df['city'].unique():
    data = df[df['city'] == city]
    plt.plot(data['day'], data['temp'], label=city)

plt.legend()
plt.show()