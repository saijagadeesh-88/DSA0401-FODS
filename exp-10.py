import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [1000, 1500, 1200, 1800, 2000]

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()