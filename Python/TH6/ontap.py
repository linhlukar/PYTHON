import numpy as np
import matplotlib.pyplot as plt

try:
    with open('D:/DATA63.txt', mode='r', encoding='utf-8') as f:
        n = f.readline().split()
        x = np.array(n)
        n = f.readline().split()
        y = np.array(n)
        x = x.astype(float)
        y = y.astype(float)
except:
    print('FILE NOT FOUND !!!')
plt.subplot(1, 3, 1)
font
plt.bar(x, y)
plt.show()

plt.subplot(1, 3, 2)
plt.hist(x, y)
plt.show()

plt.subplot(1, 3, 3)
plt.pie(x, y)
plt.show()
