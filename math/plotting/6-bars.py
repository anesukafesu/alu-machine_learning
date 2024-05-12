#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generate Data
# Plot 1
x0 = np.arange(0, 11)
y0 = x0 ** 3

# Plot 2
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

# Plot 3
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

# Plot 4
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

# Plot 5
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create Grid
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 2)

# Create title
fig.suptitle('All in One')

# Create plots
plot1 = fig.add_subplot(gs[0, 0])
plot2 = fig.add_subplot(gs[0, 1])
plot3 = fig.add_subplot(gs[1, 0])
plot4 = fig.add_subplot(gs[1, 1])
plot5 = fig.add_subplot(gs[2, :])

# Title formatting
fontsize = 6

# Plot first graph
plot1.plot(x0, y0, color='red')
plot1.set_xlim((0, 10))

# Plot the second graph
plot2.scatter(x1, y1, color='magenta')
plot2.set_title("Men's Height vs Weight", fontsize=fontsize)
plot2.set_xlabel('Height (in)', fontsize=fontsize)
plot2.set_ylabel('Weight (lbs)', fontsize=fontsize)

# Plot the third graph
plot3.set_title('Exponential Decay of C-14', fontsize=fontsize)
plot3.set_xlabel('Time (years)', fontsize=fontsize)
plot3.set_ylabel('Fraction Remaining', fontsize=fontsize)
plot3.plot(x2, y2)
plot3.set_yscale('log')
plot3.set_xlim(0, 28651)

# Plot the fourth graph
plot4.set_title('Exponential Decay of Radioactive Elements', fontsize=fontsize)
plot4.plot(x3, y31, color='red', linestyle='dashed', label='C-14')
plot4.plot(x3, y32, color='green', label='Ra-226')
plot4.set_xlim((0, 20000))
plot4.set_ylim((0, 1))
plot4.set_xlabel('Time (years)', fontsize=fontsize)
plot4.set_ylabel('Fraction Remaining', fontsize=fontsize)
plot4.legend(fontsize=fontsize)

# Plot the fifth graph
plot5.set_title('Project A', fontsize=fontsize)
plot5.hist(student_grades, range=(0, 100), bins=10, edgecolor='black')
plot5.set_ylabel('Number of Students', fontsize=fontsize)
plot5.set_ylim([0, 30])
plot5.set_xlabel('Grades', fontsize=fontsize)
plot5.set_xlim([0, 100])
x_ticks = np.arange(0, 101, 10)
plot5.set_xticks(x_ticks)

plt.show()