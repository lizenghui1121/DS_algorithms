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


# 就地方法1, 非递归
# 将原来的右子树接到左子树的最右边节点
# 将左子树插入到右子树的地方
# 考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
def flatten_2(root):
    """
    Do not return anything, modify root in-place instead.
    """
    while root:
        # 左子树为None，直接考虑下一个节点
        if not root.left:
            root = root.right
        else:
            # 找左子树最右的节点
            pre = root.left
            while pre.right:
                pre = pre.right

            pre.right = root.right
            # 将左子树插入到右子树的地方
            root.right = root.left
            root.left = None
            # 考虑下一个节点
            root = root.right


# 递归解法
def flatten_3(root):
    pre = [None]
    def helper(root):
        if not root:
            return
        flatten(root.right)
        flatten(root.left)
        root.left = pre[0]
        root.right = None
        pre[0] = root
    helper(root)


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
    flatten_2(root)
    # flatten_3(root)
    while root:
        print(root.val)
        root = root.right