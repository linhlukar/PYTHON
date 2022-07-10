"""
Sequence:
Viết chương trình nhập một số thực x và số nguyên n , tính giá trị biểu thức :

S= 2016x +x^2/3 + x^3/3^2 + ... + x^n/3^(n-1)  nếu n chẵn
S= 0 nếu n lẻ
"""

x = float(input("Nhập x : "))
n = int(input("Nhập n: "))
S = 0
if n % 2 != 0:
    S = 0
else:
    S = 2016 * x
    T = x
    M = 1
    for i in range(1,n+1):
        T = T * x
        M = M * 3
        S = S + T / M
        # S = S + x**i / (3**(i-1))

print("Giá trị biểu thức : ", S)
