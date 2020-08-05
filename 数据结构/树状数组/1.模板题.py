"""
给定一个动态更新的数组，求任意区间和
@Author: Li Zenghui
@Date: 2020-08-05 17:01
"""


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


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    pre_sum = [0]
    for num in arr:
        pre_sum.append(pre_sum[-1] + num)
    m = len(arr)
    tree_arr = FenwickTree(m)
    print(tree_arr.tree)
    for i in range(len(arr)):
        tree_arr.update(i+1, arr[i])

    print(tree_arr.tree)
    print(tree_arr.ask(3))
    print(tree_arr.ask(4) - tree_arr.ask(1))
    print(pre_sum[4] - pre_sum[1])
