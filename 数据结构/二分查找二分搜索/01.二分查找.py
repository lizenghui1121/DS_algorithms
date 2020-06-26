"""
已知一个排序数组A,和乱序数组，查找B数组元素是否在A数组是否出现
返回数组C[1,0,1,0,1]
@Author: Li Zenghui
@Date: 2020-03-29 13:21
"""


# 1.二分查找递归版
def binary_search_1(arr_a, begin, end, target):
    if begin > end:
        return False
    mid = (begin + end) // 2
    if target == arr_a[mid]:
        return True
    elif target < arr_a[mid]:
        return binary_search_1(arr_a,  begin, mid - 1, target)
    else:
        return binary_search_1(arr_a, mid+1, end, target)


# 2.二分查找循环版
def binary_search_2(arr_a, target):
    begin = 0
    end = len(arr_a)-1
    while begin <= end:
        mid = (begin + end) // 2
        if target == arr_a[mid]:
            return True
        elif target < arr_a[mid]:
            end = mid-1
        elif target > arr_a[mid]:
            begin = mid+1
    return False


def search_array(arr_a, arr_b):
    res = []
    for item in arr_b:
        # is_exist = binary_search_1(arr_a, 0, len(arr_a), item)
        is_exist = binary_search_2(arr_a, item)
        if is_exist:
            res.append(1)
        else:
            res.append(0)
    return res


if __name__ == '__main__':
    test_arr = [1, 3, 6, 8, 14, 19]
    print(binary_search_1(test_arr, 0, len(test_arr)-1, 3))
    print(binary_search_2(test_arr, 5))
    print(search_array(test_arr, [2, 4, 6, 8]))
