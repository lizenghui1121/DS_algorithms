"""
思路：
1.根节点深度遍历树，先序遍历，将结点存入path栈中，使用path_value累加value值
2.当遇到叶结点时，检查path_value是否为sum, 如果相同就把path存入res中，否则，弹出结点，path_value减去对应的结点值
3.在后续的遍历中，将该结点值，从栈中弹出，减去对应的value

@Author: Li Zenghui
@Date: 2020-03-22 17:09
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pre_order(self, root, path_value, target, path, result):
        if not root:
            return
        path_value += root.val
        path.append(root)
        if not root.left and not root.right and path_value == target:
            result.append(path[:])
        self.pre_order(root.left, path_value, target, path, result)
        self.pre_order(root.right, path_value, target, path, result)
        path_value -= root.val
        path.pop()


if __name__ == '__main__':
    result = []
    path = []
    path_value = 0
    root = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)
    t4 = TreeNode(4)

    root.left = t1
    root.right = t2
    t1.left = t3
    t1.right = t4
    s = Solution()
    s.pre_order(root, path_value, 7, path, result)
    for row in result:
        for node in row:
            print(node.val)
