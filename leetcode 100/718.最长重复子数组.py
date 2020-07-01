"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 长度最长的公共子数组是 [3, 2, 1]。
@Author: Li Zenghui
@Date: 2020-07-01 11:51
"""


# 暴力解法 O(N^3)
def findLength_1(A, B):
    res = 0
    for i in range(len(A)):
        for j in range(len(B)):
            k = 0
            while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
                k += 1
            res = max(res, k)
    return res


# 动态规划 O(N*M)
def find_legnth_2(A, B):
    # dp[i][j] 表示 A[i:] 和 B[j:] 的最长公共前缀
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    res = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
            res = max(res, dp[i][j])
    return res

# 滑动窗口
def find_legnth_3(A, B):
    def max_length(addA, addB, length):
        ret = k = 0
        for i in range(length):
            if A[addA + i] == B[addB + i]:
                k += 1
                ret = max(ret, k)
            else:
                k = 0
        return ret
    m, n = len(A), len(B)
    res = 0
    for i in range(m):
        length = min(n, m-i)
        res = max(res, max_length(i, 0, length))
    for j in range(n):
        length = min(m, n-j)
        res = max(res, max_length(0, j, length))
    return res


if __name__ == '__main__':
    test_A = [1, 2, 3, 2, 1]
    test_B = [3, 2, 1, 4, 7]
    print(findLength_1(test_A, test_B))
    print(find_legnth_2(test_A, test_B))
    print(find_legnth_3(test_A, test_B))
