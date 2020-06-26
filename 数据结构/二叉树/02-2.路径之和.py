"""

@Author: Li Zenghui
@Date: 2020-03-25 19:17
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        path_value = 0
        path = []
        res = []
        def find_sub_path(root, path_value, target, path, result):
            if not root:
                return
            path_value += root.val
            path.append(root.val)
            if not root.left and not root.right and path_value == target:
                res.append(path[:])
            find_sub_path(root.left, path_value, target, path, result)
            find_sub_path(root.right, path_value, target, path, result)
            path_value = path_value - root.val
            path.pop()
        find_sub_path(root, path_value, expectNumber, path, res)
        return res


if __name__ == '__main__':
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
    print(s.FindPath(root, 7))