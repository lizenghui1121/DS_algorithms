"""
10大排序算法
@Author: Li Zenghui
@Date: 2020-03-21 14:44
"""


# 1.插入排序
def insert_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        preindex = i - 1
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] = current
    return arr


# 2.冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


# 3.带标记的冒泡排序
def bubble_sort_flag(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = True
        if not flag:
            break
    return arr


# 4.选择排序
def select_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


# 5.希尔排序
def shell_sort(arr):
    import math
    gap = 1
    while gap < len(arr)/3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr


# 6.归并排序
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    sub_left, sub_right = arr[0: middle], arr[middle:]
    return merge(merge_sort(sub_left), merge_sort(sub_right))


def merge(arr_left, arr_right):
    res = []
    while arr_left and arr_right:
        if arr_left[0] < arr_right[0]:
            res.append(arr_left.pop(0))
        else:
            res.append(arr_right.pop(0))
    while arr_left:
        res.append(arr_left.pop(0))
    while arr_right:
        res.append((arr_right.pop(0)))
    return res


def merge_sort_2(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    sub_left, sub_right = arr[0: middle], arr[middle:]
    return merge_2(merge_sort(sub_left), merge_sort(sub_right))


def merge_2(arr_left, arr_right):
    res = []
    i = 0
    j = 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            res.append(arr_left[i])
            i += 1
        else:
            res.append(arr_right[j])
            j += 1
    while i < len(arr_left):
        res.append(arr_left[i])
        i += 1
    while j < len(arr_right):
        res.append(arr_right[j])
        j += 1
    return res


# 7.快速排序
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    test_arr1 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr2 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr3 = [2, 5, 6, 1, 4, 3, 7, 8]
    test_arr4 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr5 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr6 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr7 = [2, 5, 6, 1, 4, 8, 3, 7]
    test_arr8 = [5, 7, 11, 56, 12, 1, 9]
    test_arr9 = [2, 5, 6, 1, 4, 8, 3, 7]
    print(insert_sort(test_arr1))
    print(bubble_sort(test_arr2))
    print(bubble_sort_flag(test_arr3))
    print(select_sort(test_arr4))
    print(shell_sort(test_arr5))
    print(merge_sort(test_arr6))
    print(merge_sort_2(test_arr7))
    print(quick_sort(test_arr8, 0, len(test_arr8)-1))


