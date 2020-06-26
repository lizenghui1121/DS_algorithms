"""

@Author: Li Zenghui
@Date: 2020-04-09 22:19
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        temp = []
        for i in range(0, len(matrix), cols):
            temp.append(list(matrix[i:i + cols]))
        matrix = temp
        # write code here
        mark = [[0 for i in range(cols)] for j in range(rows)]
        count = [False]
        def backtrack(track, row, col, mark):
            mark[row][col] = 1
            track.append(matrix[row][col])
            if path == ''.join(track):
                count[0] = True
                return True
            if len(track) > len(path):
                return
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                newx = row + dx[i]
                newy = col + dy[i]
                if len(path) > len(track) and 0 <= newx < rows and 0 <= newy < cols:
                    if mark[newx][newy] == 0:
                        backtrack(track, newx, newy, mark)
                else:
                    continue
            track.pop()
            mark[row][col] = 0

        track = []
        for i in range(rows):
            for j in range(cols):
                backtrack(track, i, j, mark)
        return count[0]


if __name__ == '__main__':
    s = Solution()
    arr = 'abcesfcsadee'
    print(s.hasPath(arr, 3, 4, 'bccd'))
