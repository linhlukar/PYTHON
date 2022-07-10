"""
Bài 1.5. License Plate – Bài tổng hợp (30 phút)
Nhập vào một số nguyên n có ít hơn 6 chữ số.
 Số vừa nhập là hợp lệ nếu nó là một số nguyên tố và đối xứng
 (số nguyên tố là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó;
 số đối xứng là số mà các con số của nó có thể đọc xuôi hay người đều như nhau,
 ví dụ 132231 hay 131,...).
Ghi chú: Để dễ hơn, ta giả sử n luôn có 6 chữ số !

"""

import math


n = int(input(" Nhập n: "))

while n < 0 or n > 100000: #chừng nào mà
    n = int(input(" Nhập lại n : "))

for i in range(2, int(math.sqrt(n))+1):
     if n % i == 0:
         snt = False
     else:
         snt = True

d = 0
m = n
while n > 0:
    r = n % 10
    d = d * 10 + r
    n = n // 10
if d == m:
    dx = True
else:
    dx = False


if (snt == True and dx == True):
    print("Số vừa nhập là hợp lệ ")
else:
    print("Số vừa nhập không hợp lệ ")