import matplotlib.pyplot as plt
import numpy as np


# Vẽ biểu đồ bar với x, y trên khung hình thứ nhất
def readdata(filename):
    with open(filename, mode='r') as f:
        x = np.array(f.readline().split(' ')).astype(float)
        y = np.array(f.readline().split(' ')).astype(float)
        f.close()
        return x, y


# x, y = readdata('D:\\DATA63.txt')
# x = np.array(x)
# y = np.array(y)
# plt.subplot(1, 3, 1)
# plt.suptitle('BAR CHART')
# plt.bar(x, y)
# plt.grid(axis='y', color='g', linestyle=':', linewidth=1.5)
# plt.show()
x, y = readdata('D:/DATA63.txt')
plt.suptitle('BAR-HIST-PIE CHART')
plt.subplot(1, 3, 1)
plt.title('BAR CHART')
plt.grid(axis='y', color ='g', linestyle =':', linewidth =1.5)
plt.bar(x, y, color='r')
plt.subplot(1, 3, 2)
plt.title('HISTOGRAM CHART')
plt.grid(axis='y', color ='g', linestyle =':', linewidth =1.5)
plt.hist(y, color='b')
plt.subplot(1, 3, 3)
plt.title('PIE CHART')
plt.pie(y)
plt.show()