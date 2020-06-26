"""
一条直线，有N个房屋，每个房屋有不同数量的财宝，不能从相邻的两个房间拿财宝，问在不触发报警器的情况下，最多可获得多少财宝。
@Author: Li Zenghui
@Date: 2020-03-03 20:01
"""


class Solution:

    def rob(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([5, 2, 6, 3, 1, 7]))
