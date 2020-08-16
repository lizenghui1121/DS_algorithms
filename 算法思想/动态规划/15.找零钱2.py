"""

@Author: Li Zenghui
@Date: 2020-08-10 11:25
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        print(dp)
        return dp[amount]


if __name__ == '__main__':
    nums = [2, 5, 10]
    target = 11
    s = Solution()
    print(s.change(target, nums))