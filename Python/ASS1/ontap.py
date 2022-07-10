import numpy as np


def READ(filename):
    try:
        with open(filename, mode='r') as f:
            x = []
            while True:
                line = f.readline()
                if not line: break
                x.append(line.split('\t'))
            return np.array(x)

    except:
        print('Không có file nhé ! ')
        return


filename = 'D:/kddcup.data'
print('Đang đọc tệp !', filename, '...', end=' ')
