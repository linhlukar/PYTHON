import matplotlib.pyplot as mp
import numpy as np

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
y = np.array([20, 30, 10, 40, 20, 30, 20, 10, 40, 50])
mp.subplot(1, 2, 1)
mp.plot(x, y)

# x = np.linspace(-10, 10, 100)
# y = 3*x*x*x - 3*x*x + 3*x - 3
# mp.subplot(1,2,2)
# mp.plot(x, y)
#
# x = np.linspace(10,15,100)
# y = 2*x*x+1
# mp.subplot(1,2,2)
# mp.plot(x,y)

mp.show()
