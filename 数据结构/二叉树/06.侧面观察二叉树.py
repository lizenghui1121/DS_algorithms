"""
将结点与层数绑定为pair，压入队列时，将结点与层数同时压入队列。
@Author: Li Zenghui
@Date: 2020-03-22 20:15
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def right_side_view(root, start):
    q = []
    view = []
    if root:
        q.append([root, start])
        print(q)
        while q:
            temp = q.pop(0)
            node = temp[0]
            depth = temp[1]
            if len(view) == depth:
                view.append(node.val)
            else:
                view[depth] = node.val
            if node.left:
                q.append([node.left, depth+1])
            if node.right:
                q.append([node.right, depth+1])
    return view


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
    view = right_side_view(root, 0)
    print(view)

