"""
描述：
已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，当s>g时可以满足孩子，求使用这些糖果，最多能满足多少孩子。
@Author: Li Zenghui
@Date: 2020-03-31 16:07
"""


def find_content_children(g, s):
    """
    :param g: 数组，孩子的需求
    :param s: 数组，糖果的大小
    :return: 整型，满足的孩子个数
    """
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if g[child] < s[cookie]:
            child += 1
        cookie += 1
    return child


if __name__ == '__main__':
    g = [2, 4, 6, 8, 9, 10]
    s = [1, 3, 8, 20]
    print(find_content_children(g, s))
