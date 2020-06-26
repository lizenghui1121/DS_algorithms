"""

@Author: Li Zenghui
@Date: 2020-03-29 15:31
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


def mid_order_print(node):
    if not node:
        return
    mid_order_print(node.left)
    print(node.val)
    mid_order_print(node.right)


class Code:

    def encode(self, node):
        res = []

        def pre_order(node, s):
            if not node:
                return
            s.append(str(node.val))
            s.append('#')
            pre_order(node.left, s)
            pre_order(node.right, s)
        pre_order(node, res)
        return ''.join(res)

    def serialize(self, s):
        if not s:
            return None
        temp = s.split('#')
        nums = temp[:-1]
        print(nums)
        nodes = [TreeNode(int(i)) for i in nums]
        root = nodes[0]
        for i in range(1, len(nodes)):
            bst_insert(root, nodes[i])
        return root


if __name__ == '__main__':
    test_arr = [3, 10, 1, 6, 15]
    root = TreeNode(8)
    nodes = [TreeNode(i) for i in test_arr]
    for insert_node in nodes:
        bst_insert(root, insert_node)
    solution = Code()
    res_str = solution.encode(root)
    res_node = solution.serialize(res_str)
    # print(res_node.val)
    mid_order_print(res_node)
