"""
一个数组，求最长上升子序列的长度
@Author: Li Zenghui
@Date: 2020-03-03 21:17
"""

class Solution1:
    def lenth_of_sub(self, nums):
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        print(dp)
        return max(dp)


class Solution2:
    def length_of_sub(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        sta = []
        sta.append(nums[0])
        for i in range(1, n):
            if nums[i] >= sta[-1]:
                sta.append(nums[i])
            else:
                for j in range(len(sta)):
                    if sta[j] > nums[i]:
                        sta[j] = nums[i]
                        break
        print(sta)
        return len(sta)


if __name__ == '__main__':
    s1 = Solution1()
    print(s1.lenth_of_sub([1, 3, 2, 3, 1, 4, 2, 2, 2]))
    s2 = Solution2()
    print(s2.length_of_sub([1, 3, 2, 3, 1, 4, 2, 2, 2, 3]))