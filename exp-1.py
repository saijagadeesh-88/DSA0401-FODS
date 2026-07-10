import numpy as np
marks = np.array([
    [80, 75, 90, 85],
    [70, 60, 88, 92],
    [85, 78, 95, 89],
    [90, 82, 85, 87]
])

print("Marks Matrix:")
print(marks)

subject_avg = np.mean(marks, axis=0)

print("\nAverage score of each subject:")
print(subject_avg)

highest_avg = np.max(subject_avg)
subject_index = np.argmax(subject_avg)

print("\nHighest Average Score:", highest_avg)
print("Subject with Highest Average: Subject", subject_index + 1)