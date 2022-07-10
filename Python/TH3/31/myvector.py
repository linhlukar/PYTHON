def vecinput():
    n = int(input('n='))
    a = [0] * n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i + 1)))
    return a


def vecsum(a):
    tong = 0.0  # khởi tạo giá trị tổng ban đầu bằng 0
    for i in a[:]:
        tong += i
    return tong


def Chen(a, p, v):
    if p < 0 or p > len(a):
        print('SAIIII')
    else:
        a.insert(p, v)
    return a


def XOA(a, v):
    if a.count(v) > 0:
        a.remove(v)
    return a


a = vecinput()
print(a)
b = vecsum(a)
print(b)
c = Chen(a, 2, 100)
print('Mảng sau khi chèn: ', c)
d = XOA(c, 12)
print('Mảng sau khi xóa: ', d)
