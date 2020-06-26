"""

@Author: Li Zenghui
@Date: 2020-05-30 14:50
"""
a = []
b = []

end_count = 0
while end_count < 2:
    input_line = input()
    if end_count == 0:
        if input_line != "end":
            a.append(list(map(int, input_line.split())))
        else:
            end_count += 1
    else:
        if input_line != "end":
            b.append(list(map(int, input_line.split())))
        else:
            end_count += 1


def find_similar_matrix(a, b):
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])
    min_gap = float('inf')
    for i in range(0, a_row-b_row+1):
        for j in range(0, a_col-b_col+1):
            sub_arr = [a[k][j:j+b_col] for k in range(i, i+b_row)]
            cur_gap = get_gap_sum(sub_arr, b)
            # print(cur_gap)
            if cur_gap < min_gap:
                min_gap = cur_gap
                min_x = i
                min_y = j
    res = [a[k][min_y:min_y+b_col] for k in range(min_x, min_x+b_row)]
    for item in res:
        print(' '.join(map(str, item)))


def get_gap_sum(a, b):
    ans = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            ans += abs(a[i][j] - b[i][j])
    return ans


# print(a)
# print(b)
find_similar_matrix(a, b)
