import numpy as np

def READ (filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            n, m = f.readline().split()
            n = int(n)
            m = int(m)
            a = []
            for i in range(n):
                k = f.readline().split()
                for i in range(len(k)):
                    k[i]= float(k[i])
                a.append(k)
        return a, n, m
    except:
        print('File không hợp lệ ')

def Trungbinh(a, n, m, i):
    if i > m:
        print('Data with', m, 'colums!')
        return
    else:
        tong = 0.0
        for j in range(n):
            tong += a[j][i]
        return tong/n


a, n, m = READ('D:/DATA43.txt')
print('Số dòng=',n)
print('Số cột=',m)
print('Mảng =', a)

col = int(input('trung bình = '))
k = Trungbinh(a, n, m, col)
print('AVG =', k)