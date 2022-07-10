import numpy as np


def READ(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            n, m = f.readline().split()
            n = int(n)
            m = int(m)
            a = []
            for i in range(n):
                k = f.readline().split()
                a.append(k)
            a = np.array(a)
            return a, n, m
    except:
        print('FILE NOT FOUND')
        return


a, n, m = READ('D:/DATA54.txt')


# 2. Tách mảng data thành 2 mảng: Mảng x chứa (m-1) ccootj đầu tiên của data
# mảng y chứa cột cuối cùng của data (định dạng nguyên)
def TACH(a, n, m):
    try:

        x = a[:, :m - 1]
        y = a[:, m - 1]
        y = np.reshape(y, -1)
        y = y.astype(int)
        return x, y
    except:
        print('FILE NOT FOUND !')
        return


x, y = TACH(a, n, m)
print('Mảng x: \n', x)
print('Mảng y : \n', y)


# 3. Đếm mảng y có bao nhiêu giá trị khác nhau ?
# Mỗi giá trị xuất hiện bao nhiêu lần
def DEM(y):
    try:
        k = np.bincount(y)
        d = np.count_nonzero(k)
        print('Số phần tử khác nhau trong mảng y : ', d)
        for i in range(len(k)):
            if k[i] != 0:
                print('Phần tử ', i, 'xuất hiện ', k[i], 'lần')

    except:
        print('FILE NOT FOUND !')
        return


DEM(y)


# 4. Tính Trung bình cộng từng cột trong mảng x
# lưu trung bình cộng vào một mảng một chiều tb
def TBCcot(x):
    b = np.zeros(len(x[0]))
    for i in range(len(x[0])):
        k = x[:, i]
        k = np.reshape(k, -1)
        t = 0
        for t in range(len(k)):
            if k[t] != '?':
                b[i] += float(k[t])
            else:
                t = t + 1
            b[i] /= len(x) - t
    return b


tb = TBCcot(x)
print('Trung bình cộng từng cột : ', tb)


# 5. Thay thế ? trong mảng x bằng TBC cột tương ứng
def Thaythe(x, tb):
    n = len(x)
    m = len(x[0])
    for j in range(m):
        for i in range(n):
            if x[i, j] == '?':
                x[i, j] = tb[j]
    x = x.astype(float)
    return x


x = Thaythe(x, tb)
print('Mảng x : \n', x)


def writefile(x, y, filename1, filename2):
    with open(filename1, mode='w', encoding='utf-8') as f1:
        for i in range(len(x)):
            for j in range(len(x[0])):
                f1.write(str(x[i, j]) + ' ')
            f1.write('\n')
    with open(filename2, mode='w', encoding='utf-8') as f2:
        for i in range(y.size):
            f2.write(str(y[i]) + '\n')


writefile(x, y, 'D:/x.txt', 'D:/y.txt')


#7. Chia mảng x thành x_train và x_test
#chia mảng y thành y_train và y_test
#Lưu 4 mảng tính được vào tệp
def CHIA(x, y, type):
    n = len(x)
    n_train = int(n* type)
    n_test = n - n_train
    x_test = []
    y_test = []
    for i in range(n_test):
        pos = np.random.randint(0, n - 1)
        k = list(x[pos, :])
        x_test. append(k)
        y_test. append(y[pos])
        x = np.delete(y, pos, 0)
        y = np.delete(y, pos, 0)
        n = len(x)
    x_train = np.array(x)
    y_train = np.array(y)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    print ('ĐÃ CHIA XONG !!')
    return x_train, y_train, x_test, y_test


print(x, y)
x_train, y_train, x_test, y_test = CHIA(x, y, 0.7)
writefile(x_train, y_train, 'D:/x_train.txt', 'D:/y_train.txt')
writefile(x_test, y_test, 'D:/x_test.txt', 'D:/y_test.txt')