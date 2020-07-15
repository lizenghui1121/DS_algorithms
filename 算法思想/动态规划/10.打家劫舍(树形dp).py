"""

@Author: Li Zenghui
@Date: 2020-07-14 12:29
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob(root):
    if not root:
        return 0
    money = root.val
    if root.left:
        money += rob(root.left.left) + rob(root.left.right)
    if root.right:
        money += rob(root.right.left) + rob(root.right.right)

    return max(money, rob(root.left) + rob(root.right))


def rob2(root):
    def rob_internal(root, dic):
        if not root:
            return 0
        if root in dic:
            return dic[root]
        money = root.val
        if root.left:
            money += rob_internal(root.left.left, dic) + rob_internal(root.left.right, dic)
        if root.right:
            money += rob_internal(root.right.left, dic) + rob_internal(root.right.right, dic)
        res = max(money, rob_internal(root.left, dic) + rob_internal(root.right, dic))
        dic[root] = res
        return res
    dic = {}
    return rob_internal(root, dic)


def rob3(root):
    def robInternal(root):
        if not root:
            return [0, 0]
        res = [0, 0]
        left = robInternal(root.left)
        right = robInternal(root.right)

        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = left[0] + right[0] + root.val
        return res
    result = robInternal(root)
    return max(result[0], result[1])


if __name__ == '__main__':
    root = TreeNode(3)
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(1)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.right = n5
    print(rob(root))
    print(rob2(root))
    print(rob3(root))
