import pandas as pd

order_data = pd.DataFrame({
    'product': ['P1', 'P2', 'P1', 'P3', 'P2', 'P4', 'P5'],
    'quantity': [10, 5, 7, 3, 8, 12, 6]
})

product_sales = order_data.groupby('product')['quantity'].sum()


sorted_sales = product_sales.sort_values(ascending=False)


top_5_products = sorted_sales.head(5)

print(top_5_products)