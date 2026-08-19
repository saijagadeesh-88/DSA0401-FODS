# Question: Using Pandas DataFrame operations, how would you find the following information from
# the order_data DataFrame:
# 1. The total number of orders made by each customer.
# 2. The average order quantity for each product.
# 3. The earliest and latest order dates in the dataset.
import pandas as pd

order_data = pd.DataFrame({
    'customer': ['A', 'B', 'A', 'C', 'B'],
    'product': ['P1', 'P2', 'P1', 'P3', 'P2'],
    'quantity': [2, 5, 3, 4, 6],
    'order_date': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-01-03', '2024-01-02', '2024-01-06'])
})

orders_per_customer = order_data.groupby('customer').size()
print(orders_per_customer)

avg_quantity = order_data.groupby('product')['quantity'].mean()
print(avg_quantity)

earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

print("Earliest:", earliest_date)
print("Latest:", latest_date)
