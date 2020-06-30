"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

@Author: Li Zenghui
@Date: 2020-06-30 16:20
"""


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    p0 = 0
    p2 = len(nums) - 1
    cur = 0
    while cur <= p2:
        if nums[cur] == 0:
            nums[p0], nums[cur] = nums[cur], nums[p0]
            p0 += 1
            cur += 1
        elif nums[cur] == 2:
            nums[p2], nums[cur] = nums[cur], nums[p2]
            p2 -= 1
        else:
            cur += 1


if __name__ == '__main__':
    test_arr = [0, 1, 2, 1, 2, 0]
    sortColors(test_arr)
    print(test_arr)
