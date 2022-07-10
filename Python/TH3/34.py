def Nhap():
    n = int(input("n = "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a


def Merge_lists(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    if i < len(a):
        for t in range(i, len(a)):
            c.append(a[t])
    if j < len(b):
        for t in range(j, len(b)):
            c.append(b[t])
    return c


a = Nhap()
print(a)
a.sort()    #sắp xếp tăng
            #a.sort () = false  sắp xếp giảm
print(a)
b = Nhap()
print(b)
b.sort()
print(b)

c = Merge_lists(a, b)
print(c)
