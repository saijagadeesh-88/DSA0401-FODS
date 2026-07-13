import numpy as np

houses = np.array([
    [3, 200000],
    [4, 250000],
    [5, 300000],
    [6, 350000],
    [2, 180000],
    [5, 320000],
    [4, 260000],
    [6, 400000]
])

filtered_houses = houses[houses[:, 0] > 4]
prices = filtered_houses[:, 1]

average_price = np.mean(prices)

print("Filtered Houses (Bedrooms > 4):")
print(filtered_houses)

print("Average Sale Price:", average_price)