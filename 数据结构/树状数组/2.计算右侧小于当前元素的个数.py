"""
给定一个整数数组 nums，按要求返回一个新数组 counts。
数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

@Author: Li Zenghui
@Date: 2020-08-05 17:21
"""
from bisect import bisect_left


class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.size = n

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, k):
        # 从下到上，可以等于size
        while i <= self.size:
            self.tree[i] += k
            i += self.lowbit(i)

    def ask(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res

    def get_mapping_list(self, nums):
        return list(sorted(set(nums)))

    def discretization(self, nums):
        mapping = self.get_mapping_list(nums)
        return [bisect_left(mapping, num) + 1 for num in nums]


if __name__ == '__main__':
    # 1. 离散化处理
    nums = [5, 2, 6, 6, 1]
    m = len(nums)
    treeArr = FenwickTree(m+1)
    counts = [0] * len(nums)
    print(counts)
    nums = treeArr.discretization(nums)
    print(nums)
    for i in range(len(nums) - 1, -1, -1):
        treeArr.update(nums[i], 1)
        counts[i] = treeArr.ask(nums[i]- 1)
    print(counts)