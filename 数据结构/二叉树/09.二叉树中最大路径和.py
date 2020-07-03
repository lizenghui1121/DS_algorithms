"""
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

@Author: Li Zenghui
@Date: 2020-07-03 13:30
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def max_path_sum(self, root):
        def helper(root):
            if not root:
                return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            left_gain = max(helper(root.left), 0)
            right_gain = max(helper(root.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            price_new_path = root.val + left_gain + right_gain

            # 更新答案
            self.max_sum = max(self.max_sum, price_new_path)

            return root.val + max(left_gain, right_gain)

        helper(root)
        return self.max_sum


if __name__ == '__main__':
    root = TreeNode(-10)
    t1 = TreeNode(-2)
    t2 = TreeNode(-4)
    t3 = TreeNode(-7)
    t4 = TreeNode(-1)

    root.left = t1
    root.right = t2
    t2.left = t3
    t2.right = t4
    s = Solution()
    print(s.max_path_sum(root))