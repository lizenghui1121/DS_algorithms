"""

@Author: Li Zenghui
@Date: 2020-07-02 11:51
"""


# 重叠法，易理解
def max_rectangle(matrix):
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    datas = [0] * col
    max_area = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '0':
                datas[j] = 0
            else:
                datas[j] += 1
        sample = list(set(datas))
        print(sample)
        for idx1 in range(len(sample)):
            mlen, curlen = 0, 0
            for idx2 in range(col):
                if datas[idx2] > sample[idx1]:
                    curlen += 1
                else:
                    max_area = max(max_area, curlen * sample[idx1])
                    curlen = 0
                mlen = max(mlen, curlen)
            max_area = max(max_area, mlen * sample[idx1])
    return max_area


if __name__ == '__main__':
    test_matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(max_rectangle(test_matrix))
