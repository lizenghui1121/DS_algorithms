"""

@Author: Li Zenghui
@Date: 2020-03-22 19:29
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(root, arr):
    if not root:
        return
    arr.append(root)
    preorder(root.left, arr)
    preorder(root.right, arr)


def flatten(root):
    arr = []
    preorder(root, arr)
    for i in range(1, len(arr)):
        arr[i-1].left = None
        arr[i-1].right = arr[i]
    node = arr[0]
    while node:
        print(node.val)
        node = node.right


# 就地方法
def pre_order_2(node, last):
    if not node:
        return
    if not node.left and not node.right:
        last = node
        return
    left = node.left
    right = node.right
    left_last = None
    right_last = None

    if left:
        pre_order_2(left, left_last)
        node.left = None
        node.right = left
        last = left_last
    if right:
        pre_order_2(right, right_last)
        if left_last:
            left_last.right = right

        last = right_last


def flatten2(root):
    last = None
    pre_order_2(root, last)


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

    # flatten(root)
    flatten2(root)
    while root:
        print(root.val)
        root = root.right