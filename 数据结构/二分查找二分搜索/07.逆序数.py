"""
已知数组nums, 求新数组count, count[i]代表了在nums[i]右侧且比nums[i]小的元素数目
算法思路:
将原数组逆置后,按顺序,插入到记录左子树数量的二叉查找树中,计算已有元素有多少比当前元素小
@Author: Li Zenghui
@Date: 2020-03-29 16:06
"""


# 记录左子树结点数量的二叉排序树
class BSTNode:
    def __init__(self, x):
        self.val = x
        self.count = 0
        self.left = None
        self.right = None


def bst_insert(node, insert_node, count_small):
    if insert_node.val <= node.val:
        node.count += 1
        if node.left:
            bst_insert(node.left, insert_node, count_small)
        else:
            node.left = insert_node
    else:
        count_small[0] += node.count + 1
        if node.right:
            bst_insert(node.right, insert_node, count_small)
        else:
            node.right = insert_node


def count_smaller(nums):
    nodes = [BSTNode(i) for i in reversed(nums)]
    count = [0]
    for i in range(1, len(nodes)):
        count_small = [0]
        bst_insert(nodes[0], nodes[i], count_small)
        count.extend(count_small)
    res = count[::-1]
    return res


# 传统方法,将数组逆置,分别计算有多少比nums[i]小的数字

def count_smaller_2(nums):
    temp = nums[::-1]
    res = [0]
    for i in range(1, len(temp)):
        count = 0
        for j in range(i):
            if temp[j] < temp[i]:
                count += 1
        res.append(count)
    return res[::-1]


if __name__ == '__main__':
    test_nums = [5, -7, 9, 1, 3, 5, -2, 1]
    print(count_smaller(test_nums))
    print(count_smaller_2(test_nums))
