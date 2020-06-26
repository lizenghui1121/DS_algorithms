"""

@Author: Li Zenghui
@Date: 2020-03-03 20:27
"""


class Solution:

    def coin_change(self, coins, n):
        dp = [-1 for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != -1:
                    if dp[i] == -1 or dp[i] > dp[i-coin] + 1:
                        dp[i] = dp[i-coin] + 1
        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.coin_change([1, 2, 5, 10], 19))