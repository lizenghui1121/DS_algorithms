"""

@Author: Li Zenghui
@Date: 2020-07-25 22:56
"""


def solve(n, a):
    # write code here
    import collections
    counter = collections.Counter(a)
    res = 0
    for num in counter:
        if num != 0 and num % 2 == 0:
            while num != 1 or num != -1:
                res += 1
                num = num >> 1
    return res


if __name__ == '__main__':
    print(solve(3, [3, 2, 3]))
    print(0 % 2)
    print(2 >> 1)