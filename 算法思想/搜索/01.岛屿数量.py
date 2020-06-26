"""
描述：
用一个二维数组代表一个地图，0代表水域，1代表陆地，当水“1”在平方向或垂直方向相连时，认为是同一块土地，求小岛的数量
@Author: Li Zenghui
@Date: 2020-04-01 13:54
"""


def dfs(mark, grid, x, y):

    mark[x][y] = 1
    # 方向数组
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < 0 or newx > len(mark)-1 or newy < 0 or newy > len(mark[0])-1:
            continue
        if mark[newx][newy] == 0 and grid[newx][newy] == 1:
            dfs(mark, grid, newx, newy)


def bfs(mark, grid, x, y):
    # 方向数组
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = []
    q.append([x, y])
    mark[x][y] = 1
    while q:
        temp_point = q.pop(0)
        for i in range(4):
            newx = temp_point[0] + dx[i]
            newy = temp_point[1] + dy[i]
            if newx < 0 or newx > len(mark) - 1 or newy < 0 or newy > len(mark[0]) - 1:
                continue
            if mark[newx][newy] == 0 and grid[newx][newy] == 1:
                q.append([newx, newy])
                mark[newx][newy] = 1


def count_land_dfs(grid):
    mark = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if mark[i][j] == 0 and grid[i][j] == 1:
                dfs(mark, grid, i, j)
                count += 1
    return count


def count_land_bfs(grid):
    mark = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if mark[i][j] == 0 and grid[i][j] == 1:
                count += 1
                bfs(mark, grid, i, j)
    return count


if __name__ == '__main__':
    grid = [[1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
    print(count_land_dfs(grid))
    print(count_land_bfs(grid))
