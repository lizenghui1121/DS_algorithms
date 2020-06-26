"""
最小路径和
@Author: Li Zenghui
@Date: 2020-03-03 22:03
"""


class Solution:
    def min_path_sum(self, nums):
        row = len(nums)
        col = len(nums[0])
        dp = [[0 for i in range(col)] for i in range(row)]
        dp[0][0] = nums[0][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + nums[0][j]

        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + nums[i][0]
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
