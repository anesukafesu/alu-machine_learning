#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.title('Project A')
plt.hist(student_grades, range=(0, 100), bins=10, edgecolor='black')

plt.ylabel('Number of Students')
plt.ylim(0, 30)

plt.xlabel('Grades')
plt.xlim(0, 100)

# Plotting custom ticks
x_ticks = np.arange(0, 101, 10)
plt.xticks(x_ticks)

plt.show()