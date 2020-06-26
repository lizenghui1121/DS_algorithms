"""
给定一个排序数组(无重复元素), 且nums可能以某个未知下标旋转, 求target是否出现在旋转数组中.
@Author: Li Zenghui
@Date: 2020-03-29 14:25
"""


def search(nums, target):
    begin = 0
    end = len(nums) - 1
    nums_len = len(nums)

    while begin <= end:
        mid = (begin + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if nums[begin] < nums[mid]:
                if target > nums[begin]:
                    end = mid - 1
                else:
                    begin = mid + 1
            elif nums[begin] > nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        elif target > nums[mid]:
            if nums[begin] < nums[mid]:
                begin = mid + 1
            elif nums[begin] > nums[mid]:
                if target >= nums[begin]:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                begin = mid + 1
    return -1


if __name__ == '__main__':
    test_arr = [15, 20, 1, 5, 7, 9, 12]
    print(search(test_arr, 9))
