from math import sqrt


def Nhap():
    x = float(input('Nhap toa do x : '))
    y = float(input('Nhập tọa độ y: '))
    return x, y


def Khoangcach(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
