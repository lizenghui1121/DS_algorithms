"""

@Author: Li Zenghui
@Date: 2020-03-22 16:57
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def mid_order(root):
    if not root:
        return
    mid_order(root.left)
    print(root.val)
    mid_order(root.right)


def next_order(root):
    if not root:
        return
    next_order(root.left)
    next_order(root.right)
    print(root.val)


if __name__ == '__main__':
    root = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)
    t4 = TreeNode(5)

    root.left = t1
    root.right = t2
    t1.left = t3
    t1.right = t4

    pre_order(root)
    print("--------")
    mid_order(root)
    print("--------")
    next_order(root)
