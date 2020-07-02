"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
@Author: Li Zenghui
@Date: 2020-07-02 10:28
"""


# 暴力法 O(N^2 * logN)
def kth_smallest_1(matrix, k):
    rec = sorted(sum(matrix, []))
    return rec[k - 1]


# 归并排序，用小根堆维护，以优化时间复杂度
def kth_smallest_2(matrix, k):
    import heapq
    n = len(matrix)
    pq = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(pq)
    for i in range(k-1):
        num, x, y = heapq.heappop(pq)
        if y != n-1:
            heapq.heappush(pq, (matrix[x][y+1], x, y+1))
    return heapq.heappop(pq)[0]


# 二分查找
def kth_smallest_3(matrix, k):
    n = len(matrix)
    def check(mid):
        i, j = n-1, 0
        num = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1
        return num >= k

    left = matrix[0][0]
    right = matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(kth_smallest_1(matrix, k))
    print(kth_smallest_2(matrix, k))
    print(kth_smallest_3(matrix, k))
