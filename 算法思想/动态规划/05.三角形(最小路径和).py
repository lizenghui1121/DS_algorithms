"""

@Author: Li Zenghui
@Date: 2020-03-03 20:44
"""


class Solution:

    def mini_total(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[n-1][i] = nums[n-1][i]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + nums[i][j]
        print(dp)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.mini_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
