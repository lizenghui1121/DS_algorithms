"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例 1:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

@Author: Li Zenghui
@Date: 2020-07-16 15:04
"""


def findUnsortedSubarray1(nums):
    sorted_nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        if sorted_nums[left] == nums[left]:
            left += 1
        else:
            break
    while left <= right:
        if sorted_nums[right] == nums[right]:
            right -= 1
        else:
            break
    return right - left + 1


def findUnsortedSubarray2(nums):
    n = len(nums)
    sta = []
    left = n
    right = 0
    for i in range(n):
        while sta and nums[sta[-1]] > nums[i]:
            left = min(left, sta.pop())
        sta.append(i)
    sta = []
    for i in range(n-1, -1, -1):
        while sta and nums[sta[-1]] < nums[i]:
            right = max(right, sta.pop())
        sta.append(i)

    return right - left + 1 if right - left > 0 else 0


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(findUnsortedSubarray1(nums))
    print(findUnsortedSubarray2(nums))
