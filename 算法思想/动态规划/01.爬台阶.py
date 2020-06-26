"""

@Author: Li Zenghui
@Date: 2020-03-03 19:12
"""


class Solution:

    def climb_stair(self, n):
        if n <= 1:
            return n
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climb_stair(4))
