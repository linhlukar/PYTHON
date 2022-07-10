"""
Nhập một số nguyên có ít hơn 5 chữ số , in ra màn hình cách đọc số nguyên đó
Ví dụ : 1523 đọc là 1 ngàn 5 trăm 2 chục 3 đơn vị
"""
n = int(input('Nhập số nguyên n  : '))
while n < 0 or n >= 10000:
    n = int(input('Nhập lại n : '))
N = n // 1000
T = (n % 1000) // 100
C = (n % 100) // 10
DV = n % 10

print('{} nghìn {} trăm {} chục {} đơn vị '.format(N, T, C, DV))

# Nhập một số nguyên có ít hơn 5 chữ số, in ra màn hình cahcs đọc số nguyên đó

