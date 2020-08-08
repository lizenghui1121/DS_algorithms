"""

@Author: Li Zenghui
@Date: 2020-08-08 12:04
"""
import random
import heapq


class Solution:
    # 快速排序
    def findKthLargest(self, nums, k):
        def quickSelect(a, left, right, target):
            pivotIndex = partition(a, left, right)
            if pivotIndex == target:
                return a[pivotIndex]
            elif pivotIndex > target:
                return quickSelect(a, left, pivotIndex - 1, target)
            else:
                return quickSelect(a, pivotIndex + 1, right, target)

        def partition(a, left, right):
            randomIdx = random.randint(left, right)
            a[randomIdx], a[right] = a[right], a[randomIdx]
            index = left
            pivot = a[right]
            for i in range(left, right):
                if a[i] < pivot:
                    a[i], a[index] = a[index], a[i]
                    index += 1
            a[index], a[right] = a[right], a[index]
            return index

        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    # 优先级队列
    def find_k_largest(self, nums, k):
        q = []
        heapq.heapify(q)
        for i in range(k):
            heapq.heappush(q, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > q[0]:
                heapq.heappush(q, nums[i])
                heapq.heappop(q)
        return q[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(s.find_k_largest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
