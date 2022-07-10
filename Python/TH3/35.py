def Nhap():
    n = int(input("n = "))
    a = [0] * n
    for i in range(n):
        a[i] = input("a[{}] = ".format(i))
    return a


def Tuplefromlist(a):
    b = tuple(a)
    return b


def Dem(a):
    d = 0
    for i in range(len(a)):
        if a[i].isnumeric():
            d += 1
    return d


a = Nhap()
b = Tuplefromlist(a)
print(" Số phần tử trong b là : ", Dem(b))