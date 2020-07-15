"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

@Author: Li Zenghui
@Date: 2020-07-15 14:57
"""


def canPartition(nums):
    n = len(nums)
    nums_sum = sum(nums)
    if nums_sum & 1 == 1:
        return False

    target = nums_sum // 2
    dp = [[False] * (target + 1) for _ in range(n)]
    if nums[0] <= target:
        dp[0][nums[0]] = True

    for i in range(1, n):
        for j in range(target + 1):
            if nums[i] == j:
                dp[i][j] = True
            elif nums[i] < j:
                dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j]

    return dp[n - 1][target]


if __name__ == '__main__':
    nums = [1, 5, 5, 11]
    print(canPartition(nums))