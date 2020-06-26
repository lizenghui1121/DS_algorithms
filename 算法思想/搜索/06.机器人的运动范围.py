"""

@Author: Li Zenghui
@Date: 2020-04-06 20:04
"""


def movingCount(threshold, rows, cols):
    mark = [[0 for i in range(cols)] for j in range(rows)]
    count = [0]
    dfs(0, 0, rows, cols, mark, threshold, count)
    return count[0]


def getdigitsum(i):
    ans = 0
    while i > 0:
        ans += i % 10
        i = i//10
    return ans


def check(newx, newy, rows, cols):
    if newx < 0 or newx >= rows or newy < 0 or newy >= cols:
        return True
    return False

def dfs(h, z, rows, cols, mark, k, count):
    count[0] += 1
    mark[h][z] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        newx = h + dx[i]
        newy = z + dy[i]
        if check(newx, newy, rows, cols):
            continue
        if mark[newx][newy] == 0 and getdigitsum(newx)+getdigitsum(newy) <= k:
            dfs(newx, newy, rows, cols, mark, k, count)


if __name__ == '__main__':
    print(movingCount(10, 1, 100))
