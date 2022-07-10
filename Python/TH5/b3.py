import numpy as np


def Nhap(n, k):
    print("Nhập mảng ", k)
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(k + "[{}]=".format(i)))
    return a


def Mang2chieu(a, n):
    try:
        t = int(input("Nhập số dòng của ma trận "))
        if n % t != 0:
            raise ValueError
        k = a.reshape(t, n // t)
        return k
    except:
        print(ValueError, "Không thể shape ! ")


n = int(input("n = "))
a = Nhap(n, "a")
a = Mang2chieu(a, n)
print("Mảng a : ", a)

if a[0].any():
    b = a[:, :1]
    c = a[:, 1:2]
    b = np.reshape(b, -1)
    c = np.reshape(c, -1)

    print("Cột thứ nhât của Mảng b : ", b)
    print("Cột thứ hai của Mảng c : ", c)
d = np.concatenate(b, c)
print("Mảng d : ", d)

# cho biết vị trí các phần tử lớn hơn 1
k = np.where(d > 1)
print("vị trí các phần tử lớn hơn 1 trong c : ", k[0])

d = np.sort(d, kind="heapsort")
print ("c đã sắp ", d)

k = int (input("Nhập vào giá trị cần chèn : "))
vt = np.searchsorted(d,k)
print("Vị trí thích hợp để chèn : ", vt)
d = np.insert(d,vt, k)
print("Mảng d sau khi chèn : ", d)
