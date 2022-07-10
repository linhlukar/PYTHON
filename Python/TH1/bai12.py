# """
# Distance :
# Cho hai điểm A(x1,y1) B(x2,y2) trên mặt phẳng tọa độ Oxy. Viết chương trình nhập vào x1,x2,y1,y2.
# Tính in ra màn hình :
# - Khoảng cách Euclidean giữa A và B theo công thức D= sqrt ((x2-x1)^2+(y2-y1)^2)
# - Khoảng cách Manhattan giữa A và B :    M = |(x2-x1)| + |(y2-y1)|
# -Khoảng cách Cosin giữa A và B :  C = 1- (x1x2 + y1y2) / ( sqrt(x1^2+y1^2)| * sqrt(x2^2+y2^2))
#
# """
#
# import math
#
# x1 = float(input("nhập x1: "))
# x2 = float(input("nhập x2: "))
# y1 = float(input("nhập y1: "))
# y2 = float(input("nhập y2: "))
#
# D = math.sqrt((x2-x1)**2+(y2-y1)**2)
# M = math.fabs(x2-x1) + math.fabs(y2-y1)
# C = 1 - (x1*x2 + y1*y2) / (math.sqrt(x1**2+y1**2) * math.sqrt(x2**2+y2**2))
#
# print("Khoảng cách Euclidean : ", D)
# print("Khoảng cách Manhattan: ", M)
# print("Khoáng cách Cosin : ", C)


import numpy as np
import math
x1 = float(input("x1 = "))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
print('Tọa độ A({}, {}) '.format(x1, y1))
print('Tọa độ B({},{})'.format(x2, y2))

D = math. sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(D)

M = math.fabs(x2 - x1) + abs(y2 - y1)
print(M)

C = 1 - (x1*x2 + y1*y2)/(math.sqrt(x1**2+y1**2) * math.sqrt(x2**2+y2**2))
print(C)



