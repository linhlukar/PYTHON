def list_input():
    n = int(input("n = "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a


# duyệt trên mảng ngắn
# for i in range (len(b)):
#     c.append (a[i])

def mergelist(a, b):  # trộn mảng
    c = []
    if len(a) <= len(b):
        for i in range(len(a)):
            c.append(a[i])
            a.append(b[i])
        for t in range(i + 1, len(b)):
            c.append(b[t])
    else:
        for i in range(len(b)):
            c.append(a[i])
            a.append(b[i])
        for t in range(i + 1, len(a)):
            c.append(a[t])

a = list_input()
b = list_input()
c = mergelist(a, b)
print(c)