import numpy as np


def read(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        # Tách dữ liệu thành từng hàng và bỏ dòng cuối (vì dòng cuối là trống)
        rows = f.read().split('\n')[:-1]
        data = []
        for row in rows:
            # Tách từng phần tử trong hàng thành một mảng
            data.append(row.split('\t'))
        return data
