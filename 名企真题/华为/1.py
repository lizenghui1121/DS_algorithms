"""

@Author: Li Zenghui
@Date: 2020-04-24 14:44
"""

nums = list(map(int, input().split()))


def f(nums):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[slow] = nums[i]
            slow += 1
    for k in range(slow, len(nums)):
        nums[k] = 0
    return nums


print(f(nums))
