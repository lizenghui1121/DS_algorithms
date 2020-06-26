"""
给定一个数组nums无重复数字,给定一个target,如果出现则返回下标,如果没出现,则返回应该插入的位置,使得数组仍有序.
@Author: Li Zenghui
@Date: 2020-03-29 13:56
"""


def search_insert(nums, target):
    index = -1
    begin = 0
    end = len(nums) - 1
    while index == -1:
        mid = (begin + end) // 2
        if target == nums[mid]:
            index = mid
        elif target < nums[mid]:
            if mid == 0 or target > nums[mid-1]:
                index = mid
            end = mid -1
        elif target > nums[mid]:
            if mid == len(nums)-1 or target < nums[mid+1]:
                index = mid + 1
            begin = mid + 1
    return index


if __name__ == '__main__':
    test_arr = [1, 3, 5, 9, 14, 17, 200, 207, 500]
    print(search_insert(test_arr, 9))
    print(search_insert(test_arr, 201))
    print(search_insert(test_arr, 501))
    print(search_insert(test_arr, 0))
    print(search_insert(test_arr, 100))
