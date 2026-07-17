import pandas as pd

# Sample DataFrame
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['CityA', 'CityB', 'CityA', 'CityC', 'CityB'],
    'bedrooms': [3, 5, 2, 6, 4],
    'area': [1200, 2000, 900, 2500, 1800],
    'price': [50000, 80000, 40000, 100000, 75000]
})

# 1. Average listing price per location
avg_price = property_data.groupby('location')['price'].mean()
print("Average price per location:\n", avg_price)

# 2. Number of properties with more than 4 bedrooms
count_properties = property_data[property_data['bedrooms'] > 4].shape[0]
print("Properties with >4 bedrooms:", count_properties)

# 3. Property with the largest area
largest_property = property_data.loc[property_data['area'].idxmax()]
print("Property with largest area:\n", largest_property)