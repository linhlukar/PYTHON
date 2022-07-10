S = input("Nhập một câu : ")
Q = 'Linh'

if S.find(Q) >= 0 :
    print("Xâu '", S, "' có chứa '", Q, "'")
else:
    print("Xâu '", S, "' không chứa '", Q, "'")

P = S + Q
print("Xâu ghép : ", P)

P = P.replace('Ha', 'Ba')
print ("Xâu thay thế : ", P)
L = P.split()
D = {}
for i in range(len(L)):
    D[i] = L[i]
print[D]