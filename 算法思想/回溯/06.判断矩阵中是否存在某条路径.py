"""

@Author: Li Zenghui
@Date: 2020-04-06 17:50
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        mark = [[0 for i in range(cols)] for j in range(rows)]

        def backtrack(track, row, col, mark):
            mark[row][col] = 1
            track.append(matrix[row][col])
            if path == ''.join(track):
                return True
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                newx = row + dx[i]
                newy = col + dy[i]
                if len(path) > len(track) and 0 <= newx < rows and 0 <= newy < cols:
                    if mark[newx][newy] == 0:
                        if backtrack(track, newx, newy, mark):
                            return True
                else:
                    continue

        track = []
        for i in range(rows):
            for j in range(cols):
                has_is = backtrack(track, i, j, mark)
                if has_is:
                    return True
                # mark = [[0 for i in range(cols)] for j in range(rows)]
        return False


if __name__ == '__main__':
    s = Solution()
    mat = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(s.hasPath(mat, 3, 4, 'ABCB'))

