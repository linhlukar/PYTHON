def diccount(a):
    count = 0
    for x in a.values():
        if 2.5 <= float(x) <= 3.5:
            count += 1
    return count


def Xoa(d):
    R = {}
    for k in d.keys():
        if d[k] >= 2.0:
            R[k] = d[k]
    return R

a ={
    2020602060: 3.31,
    2020602061: 3.9,
    2020602062: 3.1,
    2020602063: 3.2}

d = diccount(a)
print('Số sv [2.5 : 3.5] là: ', d)
e = Xoa(a)
print('Mảng sau khi xóa: ', e)