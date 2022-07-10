import numpy as np


def Vecin(n, name):
    a = np.random.rand(n)
    for i in range(n):
        a[i] = int(input('{}[{}]='.format(name, i)))
    return a


def CHUYEN(a, n):
    try:
        t = int(input('t='))
        if n % t != 0:
            raise ValueError
        m = a.reshape(t, n // t)
        return m
    except:
        print('FILE NOT FOUND')


n = int(input('n='))
a = Vecin(n, 'a')
print(a)
b = CHUYEN(a, n)
print(b)

c = b[:, :1]
print(c)
# c = np.reshape(c, -1)
print(np.reshape(c, -1))

d = np.concatenate((b,c)) #câu lệnh nối
print('d = \n', d)

e = np.where(d>1)
print(e[0])
