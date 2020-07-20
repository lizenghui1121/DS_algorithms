"""
思路
两个节点的祖先结点一定出现在从根结点到这两个结点的路径上
同时出现在两条路径上的最后一个结点即为所求

@Author: Li Zenghui
@Date: 2020-03-22 18:56
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_order(node, search, path, result, finish):
    if not node or finish:
        return
    path.append(node)
    if node == search:
        finish = 1
        for i in path:
            result.append(i)
    pre_order(node.left, search, path, result, finish)
    pre_order(node.right, search, path, result, finish)
    path.pop()


# 递归解法
def lowestCommonAncestor(root, p, q):
    def dfs(root, p, q):
        nonlocal res
        if not root:
            return False
        lson = dfs(root.left, p, q)
        rson = dfs(root.right, p, q)
        if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
            res = root
        return lson or rson or (root.val == p.val or root.val == q.val)
    res = None
    dfs(root, p, q)
    return res.val


if __name__ == '__main__':
    res1 = []
    res2 = []
    path = []
    root = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)
    t4 = TreeNode(5)

    root.left = t1
    root.right = t2
    t1.left = t3
    t1.right = t4
    finish = 0
    print("递归解法", lowestCommonAncestor(root, t3, t4))
    pre_order(root, t3, path, res1, 0)
    path = []
    pre_order(root, t4, path, res2, 0)
    print(res1, res2)
    if len(res1) < len(res2):
        path_len = len(res1)
    else:
        path_len = len(res2)
    node = None
    for i in range(path_len):
        if res1[i] == res2[i]:
            node = res2[i]
    print(node.val)



