# Cho tệp dữ liệu . n: số dòng ; m : số cột, các dòng tiếp chứa bản ghi của bộ dữ liệu
import numpy as np


# 1. Đọc toàn bộ file dữ liệu lên các biến n, m, data(nxm)
def read(filename):
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
        print('FILE NOT FOUND !')
        return


a, n, m = read('D:/DATA54.txt')


# 2. Tách mảng data thành 2 mảng : Mảng x chứa (m-1) cột đầu tiên của data ,
# Mảng y chứa cột cuối cùng của data ( y được định dạng kiểu số nguyên)

def arrsplit(a, n, m):
    x = a[:, :m - 1]
    y = a[:, m - 1]
    y = np.reshape(y, -1)
    y = y.astype(int)
    return x, y


x, y = arrsplit(a, n, m)
print('Mảng x : \n', x)
print('Mảng y : \n', y)


# 3. Cho biết mảng y có bao nhiêu giá trị khác nhau ?
#    Mỗi giá trị xuất hiện bao nhiêu lần ?

def countval(y):
    k = np.bincount(y)  #
    d = np.count_nonzero(k)
    print('Số phần tử khác nhau : ', d)
    for i in range(len(k)):
        if k[i] != 0:
            print('Phần tử ', i, 'xuất hiện ', k[i], ' lần. ')


countval(y)


# 4. Tính trung bình cộng từng cột trong mảng x,
# lưu các trung bình cộng đó vào một mảng một chiều tb
def columnaverage(x):
    b = np.zeros(len(x[0]))
    for i in range(len(x[0])):
        k = x[:, i]
        k = np.reshape(k, -1)  # Định hình lại mảng ( chuyển từ 1D-2D)
        t = 0
        for t in range(len(k)):
            if k[t] != '?':
                b[i] += float(k[t])
            else:
                t = t + 1

        b[i] /= (len(x) - t)

    return b


tb = columnaverage(x)


# 5. Thay thế "?" trong mảng bằng trung bình cộng của cột tương ứng/ in ra màn

def Thaythe(x, tb):
    n = len(x)
    m = len(x[0])
    for j in range(m):
        for i in range(n):
            if x[i][j] == '?':
                x[i][j] = tb[j]
    # x = x.astype(float)
    return x


x = Thaythe(x, tb)
# x = x.astype(float)
print(x)


# 6. Lưu các mảng x và y vào tệp
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


# 7. chia mảng x thành hai mảng x_train, x-test  với tỉ lệ 70% và 30%  theo các dòng
# Mảng y chia thành 2 mảng y_train , y_test với các giá trị tương ứng của hai mảng x_train và x_test
# lưu 4 mảng tính được vào tệp
def traintestsplit(x, y, tyle):
    n = len(x)
    n_train = int(n * tyle)
    n_test = n - n_train
    x_test = []
    y_test = []
    for i in range(n_test):
        pos = np.random.randint(0, n - 1)
        k = list(x[pos, :])
        x_test.append(k)
        y_test.append(y[pos])
        x = np.delete(y, pos, 0)
        y = np.delete(y, pos, 0)
        n = len(x)
    x_train = np.array(x)
    y_train = np.array(y)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    print('ĐÃ CHIA XONG !!!')
    return x_train, x_test, y_train, y_test

# print(x)
# x_train, y_train, x_test, y_test = traintestsplit(x, y, 0.7)
# writefile(x_train, y_train, 'D:/x_train.txt',  'D:/y_train.txt')
# writefile( x_test,y_test, 'D:/x_test.txt', 'D:/y_test.txt')