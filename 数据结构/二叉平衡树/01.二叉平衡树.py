"""
二叉平衡树的实现
@Author: Li Zenghui
@Date: 2020-03-29 20:49
"""


class AVLNode:

    def __init__(self, x):
        self.val = x
        self.height = 0
        self.left = None
        self.right = None

