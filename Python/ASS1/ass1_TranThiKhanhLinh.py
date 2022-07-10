import numpy as np


# Hàm read : đọc toàn bộ dữ liệu của 1 tệp lên mảng , trả về mảng đọc được
def read(filename):
    try:
        with open(filename, mode='r') as f:
            x = []
            while True:
                n = f.readline()
                if not n:
                    break
                x.append(n.split('\t'))
            return np.array(x)
    except:
        print('Không có file nhé ! ')
        return


# Hàm distance : Tính khoảng cách Euclidean giữa hai dòng bất kỳ của x
def distance(x1, x2):
    T = 0.0
    if len(x1) == len(x2):
        for i in range(len(x1)):
            T += (x1[i] - x2[i]) ** 2
        return T
    else:
        print('Lỗi tính toán ạ !! ')
        return


# Hàm distancetoall : khoảng cách từ 1 dòng test tới tất cả các dòng của x :
def Distancetoall(x_train, test):
    d = np.zeros(len(x_train))
    for i in range(len(x_train)):
        d[i] = distance(x_train[i], test)
    return d


def predict(dis, label):
    m = min(dis[np.where(dis > 0)])
    minpos = np.where(dis == m)[0][0]
    return label[minpos]


# 2. Đọc toàn bộ file kddcup.test lên mảng x_test ;
# cắt bỏ 4 cột đầu và cột cuối cùng của x_test rồi
# chuyển mảng về kiểu thực

filename1 = "D:/KDDCUP.data"
filename2 = "D:/KDDCUP.test"

print("Đang đọc tệp !", filename1, ' ... ', end=' ')
x_train = read(filename1)
label = x_train[:, len(x_train[0]) - 1]
x_train = x_train[:, 4: len(x_train[0]) - 1]
x_train = x_train.astype(float)  # chuyển mảng về kiểu thực
print('DONE !')
print('\t', filename1, x_train.shape)

print('Đang đọc tệp !', filename2, '...', end=' ')
x_test = read(filename2)
x_test = x_test[:, 4:len(x_test[0]) - 1]
x_test = x_test.astype(float)  # chuyển mảng về kiểu thực
print('DONE !')
print('\t', filename2, x_test.shape)

# 3. Lấy 1 dòng ( đặt tên là test) bất kỳ từ mảng x_test ,
# dự đoán label của nó bằng cách : tính khoảng cách từ nó tới tất cả các dòng của x_train
# Label của test là label của dòng gần với nó nhất
# (SV tổ chức thành hàm predict với đầu vào là mảng các khoảng cách -dis và mảng label

pos = int(input('Nhận bản ghi muốn dự báo lớp : '))
if pos < 0 or pos >= len(x_test):
    print('\t Vị trí bản ghi không hợp lệ !')
else:
    print('\t Vị trí bản ghi hợp lệ ! ')
    print('Đang tính khoảng cách ..........', end='')
    test = x_test[pos]
    dis = Distancetoall(x_train, test)
    print('DONE !')
    print('Lớp của dữ liệu : ', predict(dis, label))
