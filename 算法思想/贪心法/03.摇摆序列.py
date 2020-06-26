"""
描述：
一个整数序列，如果相邻元素的差恰好正负（负正）交替出现，则认为是摇摆序列，少于2个元素的序列直接是摇摆序列
给一个随机序列，求满足摇摆序列的定义的最长子序列的长度。
示例：
序列1：[1, 7, 4, 9, 2, 5] 摇摆序列：[6, -3, 5, -7, 3]
@Author: Li Zenghui
@Date: 2020-03-31 16:20
"""


# 贪心规律：当序列有一段连续递增或者递减时候，为形成摇摆序列，只保留递增（递减）序列的首尾元素。
def wiggle_max_length(nums):
    if len(nums) < 2:
        return len(nums)
    state = 'begin'
    max_length = 1
    for i in range(1, len(nums)):
        if state == 'begin':
            if nums[i-1] < nums[i]:
                state = 'up'
                max_length += 1
            elif nums[i-1] > nums[i]:
                state = 'down'
                max_length += 1
        elif state == 'up':
            if nums[i-1] > nums[i]:
                state = 'down'
                max_length += 1
        else:
            if nums[i-1] < nums[i]:
                state = 'up'
                max_length += 1
    return max_length


if __name__ == '__main__':
    print(wiggle_max_length([1, 5, 2, 10, 9, 8]))
    print(wiggle_max_length([1, 1, 2, 3, 5, 8]))
    print(wiggle_max_length([5, 8, 3]))
