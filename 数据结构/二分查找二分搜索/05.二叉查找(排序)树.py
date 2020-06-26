"""

@Author: Li Zenghui
@Date: 2020-03-29 15:04
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_insert(node, insert_node):
    if node.val > insert_node.val:
        if node.left:
            bst_insert(node.left, insert_node)
        else:
            node.left = insert_node
    else:
        if node.right:
            bst_insert(node.right, insert_node)
        else:
            node.right = insert_node


def pre_order_print(node, layer):
    if not node:
        return

    print('----'*layer, node.val)
    pre_order_print(node.left, layer+1)
    pre_order_print(node.right, layer+1)


def mid_order_print(node):
    if not node:
        return
    mid_order_print(node.left)
    print(node.val)
    mid_order_print(node.right)


def binary_search_tree(node, target):
    if node.val == target:
        return True
    elif node.val < target:
        if node.left:
            return binary_search_tree(node.right, target)
        else:
            return False
    else:
        if node.right:
            return binary_search_tree(node.left, target)
        return False


if __name__ == '__main__':
    test_arr = [3, 10, 1, 6, 15]
    root = TreeNode(8)
    nodes = [TreeNode(i) for i in test_arr]
    for insert_node in nodes:
        bst_insert(root, insert_node)
    pre_order_print(root, 0)
    mid_order_print(root)
    print(binary_search_tree(root, 7))
