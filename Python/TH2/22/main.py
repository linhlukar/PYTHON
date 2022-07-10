import counter

mile = float(input('Nhập số dặm :'))
tien = float(input('Nhập số tiền/ dặm: '))
k = mile * tien
print('Số tiền phải trả : ', k, 'VND')
print('= {} USN'. format(counter.toUSD(k)))
print('= {} EUR '. format(counter.toEUR(k)))
print('= {} RUB'.format(counter.toRUB(k)))
print('= {} JPY'.format(counter.toJPY(k)))