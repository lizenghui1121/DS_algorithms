"""

@Author: Li Zenghui
@Date: 2020-03-22 16:57
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 颜色标记法，通用代码
def inorderTraversal(root):
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
        else:
            res.append(node.val)
    return res


# 前序遍历 递归
def pre_order(root):
    if not root:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)


# 前序遍历 迭代
def pre_order_2(root):
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        cur = stack.pop()
    return res


# 中序遍历递归方式
def mid_order(root):
    if not root:
        return
    mid_order(root.left)
    print(root.val, end=" ")
    mid_order(root.right)


# 栈方式
def mid_order_2(root):
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


# 后序遍历递归
def next_order(root):
    if not root:
        return
    next_order(root.left)
    next_order(root.right)
    print(root.val, end=" ")


# 后序遍历迭代
def next_order_2(root):
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        cur = stack.pop()
    return res[::-1]

def next_order_3(root):
    stack = []
    res = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        cur = stack.pop()
    return res[::-1]

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

    # 递归遍历
    pre_order(root)
    print("")
    mid_order(root)
    print("")
    next_order(root)
    print("")
    print("------------------------------------")

    # 栈遍历方式
    print(pre_order_2(root))
    print(mid_order_2(root))
    print(next_order_2(root))

    print("-------------------")
    # 颜色标记法
    print(inorderTraversal(root))