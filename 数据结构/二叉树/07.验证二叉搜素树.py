"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

@Author: Li Zenghui
@Date: 2020-07-02 13:04
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
def is_valid_bst(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val
        if val < lower or val > upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)


# 迭代法
def is_valid_bst_2(root):
    stack = []
    in_order = float('-inf')
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if cur.val <= in_order:
            return False
        in_order = cur.val
        cur = cur.right
    return True


if __name__ == '__main__':
    root = TreeNode(2)
    a1 = TreeNode(1)
    a2 = TreeNode(3)
    root.left = a1
    root.right = a2

    root2 = TreeNode(5)
    b1 = TreeNode(1)
    b2 = TreeNode(4)
    b3 = TreeNode(3)
    b4 = TreeNode(6)
    root2.left = b1
    root2.right = b2
    b2.left = b3
    b2.right = b4
    print(is_valid_bst(root))
    print(is_valid_bst_2(root2))