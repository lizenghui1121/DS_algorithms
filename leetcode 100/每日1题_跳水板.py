"""

@Author: Li Zenghui
@Date: 2020-07-08 09:25
"""


# 回溯法-超时
def diving_board(shorter, longer, k):
    res = []
    if k == 0:
        return res
    if shorter == longer:
        return [shorter * k]

    def backtrack(depth, path_value):
        if depth == k:
            res.append(path_value)
            return
        backtrack(depth + 1, path_value+shorter)
        backtrack(depth + 1, path_value+longer)

    backtrack(0, 0)
    return list(set(res))


# 数学法
def diving_board_2(shorter, longer, k):
    if k == 0:
        return []
    if shorter == longer:
        return [shorter*k]
    gap = longer - shorter
    return [(shorter*k + gap * i) for i in range(k+1)]


if __name__ == '__main__':
    print(diving_board(1, 2, 3))
    print(diving_board_2(1, 2, 3))
