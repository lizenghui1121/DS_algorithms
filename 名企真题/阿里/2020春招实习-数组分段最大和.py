"""

@Author: Li Zenghui
@Date: 2020-05-28 21:48
"""

temp = list(map(int, input().split()))
n = temp[0]
nums = temp[1:]
print(n, nums)


def find_sub_max(n, nums):
    # dp[i][j]代表前i个元素，j个子段的最大和，第j个子段包含第i个元素
    m = len(nums)
    dp = [[0 for i in range(m)] for j in range(n)]

    for i in range(1, m):
        for j in range()
