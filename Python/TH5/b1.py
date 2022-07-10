import numpy as np

n = int(input("n="))
a = np.random.rand(n)
print("a=", a)

print("Số chiều của a : ", a.ndim)
print("Kích thước của a : ", a.shape)
print("Độ dài của a : ", len(a))
print("Kích thước của một phần tử trong a : ", a.itemsize, 'byte')
print("Số giá trị của a (Số phần tử) : ", a.size)
print("Mảng a kiểu : ", a.dtype)

#Mảng b 100 phần tử trong đoạn 1:n
b = np.linspace(1, n, 100)
print("Mảng b : ", b)
print("Số chiều của b : ", b.ndim)
print("Kích thước của b : ", b.shape)
print("Độ dài của b : ", len(b))
print("Kích thước của một phần tử trong b : ", b.itemsize)
print("Kiểu của mảng b : ", b.dtype)

c = np.arange(2, 201, 2)
print("Mảng c : ", c)

# d. Khởi tạo mảng d với 100 phần tử 1, in ra màn hình
d = np.ones(100)
print("Mảng d : ", d)
# e. Khởi tạo mảng e với 100 phần tử 0
e = np.zeros(100)
print("Mảng e : ", e)
# h. Khởi tạo mảng h với 100 phần tử theo phân bố Gauss
h = np.random.randn(100)
print("Mảng h : ", h)
# k.Khởi tạo một ma trận k gồm nxm số 1
m = int(input("m="))
k = np.ones((n, m))
print("Mảng k : ", k)
# Khởi tạo ma trận p là ma trận đơn vị
p = np.eye(n)
print("Mảng p : ", p)
# Khởi tạo ma trận đường chéo p với các giá trị trên đường chéo là mảng a
q = np.diag(a)
print("Mảng q : ", q)
