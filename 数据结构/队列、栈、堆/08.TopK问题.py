"""
在未排序的数组中,找到第K个最大的元素
示例:
输入: [3, 2, 1, 5, 6, 4] 和 K=2
输出: 5
@Author: Li Zenghui
@Date: 2020-03-29 21:40
"""
import heapq


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    print(find_kth_largest(arr, 2))
