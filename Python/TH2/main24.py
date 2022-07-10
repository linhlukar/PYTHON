from bai24 import Khoangcach

def Check(x1, y1, x2, y2, x3, y3):
    d1 = Khoangcach(x1, y1, 0, 0)
    d2 = Khoangcach(x2, y2, 0, 0)
    d3 = Khoangcach(x3, y3, 0, 0)
    k = d1
    if d2 > k:
        k = d2
    if d3 > m:
        k == d3
    if k == d1:
        return 'Điểm O gần A nhất'
    if k == d2:
        return 'Điểm B gần A nhất'
    return 'Điểm C gần A nhất'
