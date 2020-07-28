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

def top_k(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    print(min_heap)
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappushpop(min_heap, nums[i])
            # heapq.heapreplace(min_heap, nums[i])
    return min_heap[0]


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 6, 4]
    print(find_kth_largest(arr, 2))
    print(top_k(arr, 2))
