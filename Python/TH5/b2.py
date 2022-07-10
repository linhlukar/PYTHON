import numpy as np


def Nhap(n, k):
    print("Nhập mảng ", k)
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(k + "[{}]=".format(i)))
    return a


n = int(input("n = "))
a = Nhap(n, 'a')
b = Nhap(n, 'b')

print("Mảng a : ", a)
c = a + b
print("Mảng c : ", c)

d = a - b
print("Mảng d : ", d)

e = a * b
print("Mảng e : ", e)

f = a / b
print("Mảng f : ", f)

print("Tổng các phần tử của c : ", c.sum())

print("Giá trị lớn nhất của mảng c : ", c.max())

print("Giá trị nhỏ nhất của mảng c : ", c.min())

# Lấy các phần tử có chỉ số chẵn trong c , tính tổng của chúng??
k = c[0::2]
print("Các phần tử có chỉ số chẵn trong c: ", k)
print("Tổng các phần tử : ", k.sum())

# Chuyển mảng c thành mảng hai chiều
try:
    t = int(input("Nhập số dòng của ma trận : "))
    if n % t != 0:
        raise ValueError  # nếu không thể
    k = c.reshape(t, n // t)  # n chia t lấy nguyên
    print("Ma trận thu được : \n", k)
except:
    print(ValueError, "Không thể reshape ! ")  # nếu lỗi thì bị lỗi ở dòng 43
