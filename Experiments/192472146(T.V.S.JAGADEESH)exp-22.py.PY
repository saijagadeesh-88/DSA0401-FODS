Question:
"What is the 95% confidence interval for the mean reduction in blood pressure for patients who
received the new drug? Also, what is the 95% confidence interval for the mean reduction in blood
pressure for patients who received the placebo?
import pandas as pd
import scipy.stats as stats
import numpy as np

df = pd.read_csv("Q22.csv")

# Separate groups
drug = df[df['group'] == 'drug']['reduction']
placebo = df[df['group'] == 'placebo']['reduction']

# Function for CI
def confidence_interval(data):
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
    return ci

print("Drug CI:", confidence_interval(drug))
print("Placebo CI:", confidence_interval(placebo))
