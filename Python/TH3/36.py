def Nhap():
    n = int(input("n = "))
    a = [0] * n
    for i in range(n):
        a[i] = input("a[{}] = ".format(i))
    return tuple(a)


a = Nhap()
print(a)


b = tuple(float(i) for i in a[:])
print(b)


def tbc(a):
    T = 0
    for i in b[:]:
        T += 1
    return T / len(a)


print("TBC = ", tbc(b))
