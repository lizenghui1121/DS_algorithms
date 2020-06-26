"""

@Author: Li Zenghui
@Date: 2020-04-08 17:42
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold <= 0:
            return 0
        mark = [[0 for i in range(cols)] for j in range(rows)]
        count = [0]
        self.dfs(0, 0, rows, cols, mark, threshold, count)
        return count[0]


    def check(self, newx, newy, rows, cols):
        if newx < 0 or newx >= rows or newy < 0 or newy >= cols:
            return True
        return False

    def dfs(self, h, z, rows, cols, mark, k, count):
        count[0] += 1
        mark[h][z] = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            newx = h + dx[i]
            newy = z + dy[i]
            if self.check(newx, newy, rows, cols):
                continue
            if mark[newx][newy] == 0 and self.getdigitsum(newx) + count[0] < k:
                self.dfs(newx, newy, rows, cols, mark, k, count)
