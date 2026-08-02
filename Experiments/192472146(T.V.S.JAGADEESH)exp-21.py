import pandas as pf

import numpy as nf


inf=pf.read_csv("age_fat.csv")

#print(inf)

f_mean=inf.mean()
print("mean:",f_mean)
f_median=inf.median()

print("median:",f_median)
f_std=inf.std()

print("std:",f_std)

import matplotlib.pyplot as plt


plt.scatter(inf['age'], inf['fat'])
plt.xlabel("Age")
plt.ylabel("% fat")
plt.title("Age vs Fat")
plt.show()



