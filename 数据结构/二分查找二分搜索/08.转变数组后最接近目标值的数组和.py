"""

@Author: Li Zenghui
@Date: 2020-08-01 15:25
"""


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = 0
        for num in arr:
            right = max(num, right)

        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if self.calc(arr, mid) >= target:
                mid = right
            else:
                mid = left + 1

        sum1 = self.calc(arr, left)
        sum2 = self.calc(arr, left - 1)
        if sum1 - target > target - sum2:
            return left - 1
        return left

    def calc(self, arr, mid):
        ans = 0
        for num in arr:
            ans += min(num, mid)
        return ans
