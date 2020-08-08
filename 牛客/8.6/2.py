"""

@Author: Li Zenghui
@Date: 2020-08-06 20:58
"""


#
# 返回所求中序序列
# @param n int整型 二叉树节点数量
# @param pre int整型一维数组 前序序列
# @param suf int整型一维数组 后序序列
# @return int整型一维数组
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructFromPrePost(pre, post):
    if not pre: return None
    root = TreeNode(pre[0])
    if len(pre) == 1: return root

    L = post.index(pre[1]) + 1
    root.left = constructFromPrePost(pre[1:L + 1], post[:L])
    root.right = constructFromPrePost(pre[L + 1:], post[L:-1])
    return root


class Solution:
    def solve(self, n, pre, suf):
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            res.append(root.val)
            in_order(root.right)

        res = []
        root = constructFromPrePost(pre, suf)
        in_order(root)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solve(5,[3,2,1,4,5],[1,5,4,2,3]))