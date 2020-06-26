"""
给定排序数组nums, 如果target在数组中出现, 则返回区间左右端点[i, j], 否则返回[-1, -1]
@Author: Li Zenghui
@Date: 2020-03-29 14:08
"""


def search_range(nums, target):
    left = left_bound(nums, target)
    right = right_bound(nums, target)
    return [left, right]


def left_bound(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if target == nums[mid]:
            if mid == 0 or target > nums[mid - 1]:
                return mid
            end = mid - 1
        elif target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            begin = mid + 1
    return -1


def right_bound(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if target == nums[mid]:
            if mid == len(nums)-1 or target < nums[mid+1]:
                return mid
            begin = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            begin = mid + 1
    return -1


if __name__ == '__main__':
    test_nums = [1, 2, 5, 8, 8, 8, 8, 9, 10]
    print(search_range(test_nums, 8))
    print(search_range(test_nums, 7))
    print(search_range(test_nums, 5))
