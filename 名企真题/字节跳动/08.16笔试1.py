"""

@Author: Li Zenghui
@Date: 2020-08-16 11:10
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n = int(input())

pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))

res = [0]

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)
    root.left = buildTree(preorder[1:], inorder[:root_index])
    root.right = buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
    if not root.left and not root.right:
        res[0] += 1
    return root

buildTree(pre_order, in_order)
print(res[0])
