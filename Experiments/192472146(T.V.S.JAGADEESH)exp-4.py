# Question: Using NumPy arrays and arithmetic operations calculate the total sales for the year and
# determine the percentage increase in sales from the first quarter to the fourth quarter?
import numpy as np

sales_data = np.array([10000, 15000, 20000, 25000])

total_sales = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales:", total_sales)
print("Percentage Increase (Q1 to Q4):", percentage_increase, "%")
