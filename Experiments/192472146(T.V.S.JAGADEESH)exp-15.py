# Question: Write a python program will take in a dataset containing daily temperature readings for each
# city over a year and perform the following tasks:
# 1. Calculate the mean temperature for each city.
# 2. Calculate the standard deviation of temperature for each city.
# 3. Determine the city with the highest temperature range (difference between the highest and lowest
# temperatures).
# 4. Find the city with the most consistent temperature (the lowest standard deviation).
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Q15.csv")

for city in df['city'].unique():
    data = df[df['city'] == city]
    plt.plot(data['day'], data['temp'], label=city)

plt.legend()
plt.show()
