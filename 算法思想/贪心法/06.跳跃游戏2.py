"""

@Author: Li Zenghui
@Date: 2020-03-31 19:41
"""


def min_jump(nums):
    if len(nums) < 2:
        return 0
    max_index = 0
    end = 0
    jump = 0
    for i in range(len(nums)):
        max_index = max(max_index, i+nums[i])
        if end == i:
            jump += 1
            end = max_index
    return jump


def jump(nums):
    if len(nums) < 2:
        return 0
    min_jump = 1
    current_max_index = nums[0]
    pre_max_index = nums[0]
    for i in range(1, len(nums)):
        if i > current_max_index:
            min_jump += 1
            current_max_index = pre_max_index
        if pre_max_index < nums[i] + i:
            pre_max_index = nums[i] + i
    return min_jump


if __name__ == '__main__':
    print(min_jump([1]))
    print(jump([1, 2, 3, 5, 2, 1, 2]))
