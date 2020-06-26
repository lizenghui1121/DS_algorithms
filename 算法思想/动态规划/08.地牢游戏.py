"""

@Author: Li Zenghui
@Date: 2020-03-03 22:19
"""


class Solution:
    def min_hp(self, nums):
        row = len(nums)
        col = len(nums[0])
        dp = [[1 for i in range(col)] for i in range(row)]
        dp[-1][-1] = max(1, 1-nums[-1][-1])
        for i in range(row-2, -1, -1):
            dp[i][col-1] = max(1, dp[i+1][col-1]-nums[i][col-1])
        for j in range(col-2, -1, -1):
            dp[row-1][j] = max(1, dp[row-1][j+1]-nums[row-1][j])
        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                dpmin = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, dpmin-nums[i][j])
        print(dp)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.min_hp([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
