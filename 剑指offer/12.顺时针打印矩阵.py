"""

@Author: Li Zenghui
@Date: 2020-03-22 15:51
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
                if matrix:
                    res += matrix.pop()[::-1]
                if matrix and matrix[0]:
                    for row in matrix[::-1]:
                        res.append(row.pop(0))
        return res


class Solution2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix_2(self, matrix):
        # write code here
        res = []
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return res
        left = 0
        right = col-1
        top = 0
        bottom = row-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    test_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    s = Solution()
    s2 = Solution2()
    print(s2.printMatrix_2(test_arr))





