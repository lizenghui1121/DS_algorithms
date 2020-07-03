"""

@Author: Li Zenghui
@Date: 2020-07-03 11:45
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order(root):
    if not root:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)
    root.left = buildTree(preorder[1:], inorder[:root_index])
    root.right = buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
    return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    pre_order(root)
