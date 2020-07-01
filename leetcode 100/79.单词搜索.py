"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

@Author: Li Zenghui
@Date: 2020-07-01 16:07
"""


def exist(board, word):
    def dfs(board, x, y, word, used, path):
        if ''.join(path) == word:
            return True
        used[x][y] = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < row and 0 <= newy < col and used[newx][newy] == 0 and word[len(path)] == board[newx][newy]:
                path.append(board[newx][newy])
                if dfs(board, newx, newy, word, used, path):
                    return True
        used[x][y] = 0
        path.pop()

    row = len(board)
    col = len(board[0])
    used = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            path = []
            if board[i][j] == word[0]:
                path.append(board[i][j])
                flag = dfs(board, i, j, word, used, path)
                if flag:
                    return True
    return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABSF"
    print(exist(board, word))
