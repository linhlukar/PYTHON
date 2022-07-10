import matplotlib.pyplot as plt
import numpy as np

with open('D:/DATA63.txt', 'r') as f:
    n = f.readline().split()
    x = np.array(n)
    n = f.readline().split()
    y = np.array(n)
    x = x.astype(float)
    y = y.astype(float)

plt.title('SCATTER CHART')
plt.xlabel('Trục x', loc='right')
plt.ylabel('Trục y', loc='top')
plt.grid(axis='y', color='g', ls='--', lw='0.5')
plt.scatter(x, y, color='r', s=y* 2)
plt.show()
