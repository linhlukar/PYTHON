def Read(file_name):
    with open(file_name, mode= 'r', encoding='utf-8') as f:
        n, m = f.readline().split()
        print (a, m)
        n = int(n )
        for i in range (n):
            print (f.readline())

def Readtvariable(file_name):
    a = []
    n = m = 0
    with open(file_name)