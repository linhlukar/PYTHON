def list_input():
    n = int(input("n = "))
    a = [0] * n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a


def matrix_from_list(a):
    n = int(input("n = "))
    m = int(input("m = "))
    b = []
    if n * m > len(a):
        print("Can't create matrix")
    else :
        k = [0] * m       #list k là một dòng trong ma trận
        for i in range (n): #có n dòng trong ma trận
            k = a[i*m:i*m + m]
            b.append(k)   #thêm dòng k vào ma trận
        return b


a = list_input()
print (a)
b = matrix_from_list(a)
print ("matrix", b)

