"""

@Author: Li Zenghui
@Date: 2020-07-18 21:34
"""


def tree1(a):
    n = len(a)
    res = 0
    for i in range(n, 1, -1):
        res += a[i - 1] ^ a[i // 2 - 1]
    return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(tree1(a))