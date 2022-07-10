import matplotlib.pyplot as mp
import numpy as np
import math
x = np.linspace(-10,10, 100)
y = np.sin(x)
font = {'family':'consolas','color':'blue','size':14}
mp.title("ĐỒ THỊ Y = SIN(X)")
mp.xlabel("Trục X", loc='right', fontdict=font)
mp.ylabel("Trục Y", loc='top', fontdict=font)
mp.plot(x, y, marker='*', ms=10, mec='r', mfc = 'y')
mp.show()