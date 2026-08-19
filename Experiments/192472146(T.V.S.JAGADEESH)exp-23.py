# Question:
# "Based on the data collected from the A/B test, is there a statistically significant difference in the mean
# conversion rates between website design A and website design B?"
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("Q23.csv")

A = df[df['group'] == 'A']['conversion_rate']
B = df[df['group'] == 'B']['conversion_rate']

# T-test
t_stat, p_value = ttest_ind(A, B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("No significant difference")
