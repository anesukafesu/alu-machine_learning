#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Creating the data
np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Creating the labels and options
names = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', 'orange', '#ffe5b4']
fruit_names = ['apples', 'bananas', 'oranges', 'peaches']
x = [1, 2, 3]

# Initialising bottoms array
bottoms = np.zeros(fruit.shape[1])

# Plot title
plt.title('Number of Fruit Per Person')

# Plotting each fruit
for i in range(fruit.shape[0]):
  color = colors[i]
  fruit_name = fruit_names[i]
  height = fruit[i]

  plt.bar(x, height=height, bottom=bottoms, color=color, width=0.5, tick_label=names, label=fruit_name)
  bottoms += height

plt.ylim(0, 80)
plt.ylabel('Quantity of Fruit')
plt.legend()
plt.show()