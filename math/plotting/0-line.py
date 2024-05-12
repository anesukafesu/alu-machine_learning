#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11)
y = x ** 3

# your code here
plt.plot(x, y, color='red')
plt.xlim(0, 10)
plt.show()