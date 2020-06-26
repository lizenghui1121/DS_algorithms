"""
描述：
一个数组，存着非负整型数据，数组第i个元素，代表了从数组第i个位置，
最多向前跳跃nums[i]步，已知数组各元素下，求是否可以从数组第0各位置跳到数组的最后一个位置
@Author: Li Zenghui
@Date: 2020-03-31 17:56
"""


def can_jump_1(nums):
    index = [i+nums[i] for i in range(len(nums))]
    print(index)
    jump = 0
    max_index = index[0]
    while jump < len(nums) and jump <= max_index:
        if max_index < index[jump]:
            max_index = index[jump]
        jump += 1
    if jump == len(nums):
        return True
    return False


def can_jump_2(nums):
    max_index = 0
    for i in range(len(nums)):
        max_index = max(max_index, i+nums[i])
        if max_index <= i:
            return False
    if max_index >= len(nums)-1:
        return True


if __name__ == '__main__':
    print(can_jump_1([1, 2, 1, 0, 1, 4, 2]))
    print(can_jump_2([1, 2, 1, 1, 1, 4, 2]))
