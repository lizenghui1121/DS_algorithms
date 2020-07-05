"""

@Author: Li Zenghui
@Date: 2020-07-05 11:38
"""


def num(mat):
    m = len(mat)
    n = len(mat[0])
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, n+1):
        if mat[0][i-1] == 1:
            dp[i] = dp[i-1] + (i+1)
        else:
            dp[i] = dp[i-1]

    for j in range(1, m+1):
        if mat[j-1][0] == 1:
            dp[j] = dp[j]
