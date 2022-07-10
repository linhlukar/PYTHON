import matplotlib.pyplot as mp
import numpy as np

label = ['Nhãn', 'Xoài', 'Dứa', 'Chuối', 'Cam', 'Bưởi']
data = np.array([5800, 3200, 1200, 1700, 2400, 980])
explode = [0.2, 0, 0.3, 0.2, 0.1, 0]
colors = ("orange", "cyan", "brown", "grey", "indigo", "beige")
wp = {'linewidth': 1, 'edgecolor': "green"}  # độ rộng và màu của viền
mp.title('BIỂU ĐỒ SẢN LƯỢNG 2022')
mp.pie(data, labels=label, explode=explode,  colors=colors, wedgeprops=wp,
       shadow=True, autopct='%.2f')
mp.show()
