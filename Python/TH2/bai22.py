USD = 23000
EUR = 26000
RUB = 170
JPY = 190


def toUSD(n):
    return n / USD


def toEUR(n):
    return n / EUR


def toRUB(n):
    return n / RUB


def toJPY(n):
    return n / JPY


mile = float(input('Nhập số dặm :'))
tien = float(input('Nhập số tiền/ dặm: '))
k = mile * tien
print('Số tiền phải trả : ', k, 'VND')
print('= {} USN'.format(toUSD(k)))
print('= {} EUR '.format(toEUR(k)))
print('= {} RUB'.format(toRUB(k)))
print('= {} JPY'.format(toJPY(k)))
