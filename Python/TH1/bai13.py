# """
# Equations :
# Viết chương trình giải và biện luận phương trình bậc hai với các hệ số a,b,c nhập từ bàn phím
# Chú ý biện luận trong trường hợp phương trình nhập vào không phải là bậc hai
# """
#
# import math
#
# a = float(input("Nhập hệ số a : "))
# b = float(input("Nhập hệ số b : "))
# c = float(input("Nhập hệ số c : "))
#
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("Phương trình vô số nghiệm ")
#         else:
#             print("Phương trình vô nghiệm ")
#     else:
#         print("Phương trình có nghiệm x= ", -c/b)
# else:
#     delta = b*b - 4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm ")
#     elif delta == 0:
#         print("Phương trình có nghiệm kép: ", -b/(2*a))
#     else:
#         print("Phương trình có 2 nghiệm phân biệt: ")
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print("x1= ", x1)
#         print("x2= ", x2)
import math as m

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
print('Phương trình bậc hai dạng : {}x^2 + {}x + {} = 0'.format(a, b, c))
if a == 0:
    print('Phương trình bậc nhất !')
else:
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        print('Phương trình có một nghiệm : ', -c / b)
    elif delta < 0:
        print('Phương trình vô nghiệm ! ')
    else:
        print('x1 = {}'.format((-b - m.sqrt(delta)) / (2 * a)))
        print('x2 = {}'.format((-b + m.sqrt(delta)) / (2 * a)))
