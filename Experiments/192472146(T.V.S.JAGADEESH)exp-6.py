# Question: Use arithmetic operations to calculate the total cost of a customer's purchase, including
# discounts and taxes, given the item prices, quantities, discount rate, and tax rate?
import numpy as np

prices = np.array([50, 30, 20])
quantities = np.array([2, 3, 5])

discount_rate = 10   # 10%
tax_rate = 5         # 5%
total = np.sum(prices * quantities)
discount_amount = total * (discount_rate / 100)
after_discount = total - discount_amount
tax_amount = after_discount * (tax_rate / 100)
final_total = after_discount + tax_amount

print("Total before discount:", total)
print("Final Total after discount and tax:", final_total)
