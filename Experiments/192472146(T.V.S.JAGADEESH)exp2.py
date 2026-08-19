# Question: How would you find the average price of all the products sold in the past month? Assume
# 3x3 matrix with each row representing the sales for a different product
import numpy as np


sales_data = np.array([
    [250, 260, 255],   
    [400, 420, 410],   
    [150, 155, 160]    
])

overall_average_price = np.mean(sales_data)

average_price_per_product = np.mean(sales_data, axis=1)

print("Sales Data Matrix:\n", sales_data)
print("\nAverage price per product (row-wise):", average_price_per_product)
print("\nOverall average price of all products sold:", overall_average_price)
