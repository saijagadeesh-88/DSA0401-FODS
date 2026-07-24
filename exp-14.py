import matplotlib.pyplot as plt
import numpy as np

study_time = [1, 2, 3, 4, 5, 6]
scores = [40, 50, 60, 65, 70, 80]

# Scatter Plot
plt.scatter(study_time, scores)
plt.title("Study Time vs Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Scores")
plt.show()

# Correlation
correlation = np.corrcoef(study_time, scores)[0,1]
print("Correlation:", correlation)