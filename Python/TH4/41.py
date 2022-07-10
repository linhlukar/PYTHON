# def Nhap():
#     n = int(input("Nhập n : "))
#     m = int(input("Nhập m : "))
#     a = []
#     for i in range(n):
#         k = [0]*m
#         for j in range(m):
#           k[j] = float (input('a[{}][{}] = '.format(i, j)))
#         a.append(k)
#     return a
#
# def write_file(a):
#     f = open('D:/MATRIX.txt', mode='w')
#     f.write(str(len(a)) + " ")
#     f.write(str(len(a[0])) + "\n")
#
#     for i in range(len(a)):
#         for j in range (len(a[0])):
#             f.write(str(a[i][j]) + ' ')
#         f.write('\n')
#     f.close ()
#
# a = Nhap()
# print(a)
# write_file(a)
#
"""
Nhập vào từ bàn phím một ma trận a(nxm) số thực và xuất ma trận vào tệp văn bản theo định dạng :
  Dòng 1 : Chứa hai số nguyên n, m
  Các dòng khác : Chứa các dòng của ma trận
"""


def Nhap():
    n = int(input('Nhập số dòng : '))
    m = int(input('Nhập số cột : '))
    a = []
    for i in range(n):
        k = [0] * m
        for j in range(m):
            k[j] = float(input('Ma trận a[{},{}] = '.format(i + 1, j + 1)))
        a.append(k)
    return a


def WriteFile(a):
    f = open('D:/MATRIX.txt', mode='w')
    f.write('n ='+str(len(a)) + ' ')  # ghi số dòng
    f.write('m = '+str(len(a[0])) + '\n')  # ghi số cột

    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + ' ')
        f.write('\n')
    f.close()


a = Nhap()
print(a)
WriteFile(a)
