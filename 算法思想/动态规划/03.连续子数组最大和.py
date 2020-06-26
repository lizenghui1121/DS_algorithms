"""

@Author: Li Zenghui
@Date: 2020-03-03 20:15
"""


class Solution:
    def max_sub_array(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
