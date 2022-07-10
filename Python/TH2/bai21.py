import math

#ktra nguyên tố
def SNT(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0 :
                return False
        return True
    return False
a = int(input('Nhập số nguyên a : '))
if SNT(a):
    print('a là số nguyên tố ')
else :
    print('a hông là số nguyên tố')



#ktra đối xứng


"""

def isSymmetry(n):
    n1 = 0
    temp = n
    while n > 0:
        r = n % 10
        n1 = n1 * 10 + r
        n = n // 10
    if temp == n1:
        return True
    return False

# """
# def isSymmetry(n):
#     k = 8
#     while n // (10 ** k) == 0:
#         k = k - 1
#     t = (k + 1) // 2
#
#     for j in range(1, t + 1):
#         if n % 10 == n // (10 ** k):
#             n = n % (10 ** k) // 10
#             k = k - 2
#         else:
#             return False
#     return True
#
# n = int(input("Nhập số n : "))
#
# if isPrime(n):
#     print("Là số nguyên tố")
# else:
#     print("Không là sô nguyên tố")
#
# a = int(input("nhập số a: "))
# if isSymmetry(a):
#     print("Không là số đối xứng")
# else:
#     print("Là số đối xứng")
#
#
# S = int(input("Nhập số S : "))
# E = int(input("Nhập số E : "))
# while S > E or E >= 100000000:
#     S = int(input("Nhập lại S : "))
#     E = int(input("Nhập lại E : "))
#
# sum = 0
# for i in range(S, E+1):
#     if isPrime(i) and isSymmetry(i):
#         sum = sum + i
# print("Tổng các snt: ", sum)
