"""

@Author: Li Zenghui
@Date: 2020-03-17 19:48
"""

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    dp = [[0 for j in range(b+1)] for i in range(a+1)]
    for i in range(a+1):
        dp[i][1] = 1
    for j in range(b+1):
        dp[0][j] = 1
        dp[1][j] = 1

    for i in range(2, a+1):
        for j in range(1, b+1):
            if i >= j:
                dp[i][j] = dp[i][j-1] + dp[i-j][j]
            else:
                dp[i][j] = dp[i][j-1]
    print(dp[a][b])
