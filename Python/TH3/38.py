
# Cho biết có bao nhiêu sinh viên có điểm tổng kết trong đoạn [2.5 , 3.5]
def dictcount(d):
    count = 0
    for x in d.values():
        if 2.5 <= float(x) <= 3.5:
            count += 1
    return count


# Bổ sung thêm 1 sinh viên vào từ điển
def add(d):
    x = int(input("Nhâp mã sinh viên mới : "))
    y = int(input("Nhập điểm : "))
    d[x] = y
    return d


# Xóa mục thỏa mẫn điều kiện Trích ra các item không thỏa mãn điều kiện
def Xoa(d):
    R = {}
    for k in d.keys():
        if d[k] > 2.0:
            R[k] = d[k]
    return d

a = {123: 3,
     111: 5,
     456: 7,
     222: 2,
     444: 4,
     546: 2.6
     }

d = dictcount(a)
print(d)
e = add(a)
print(a)
f = Xoa(a)
print(f)
