"""

@Author: Li Zenghui
@Date: 2020-07-18 21:27
"""


def work(n):
    res = 0
    i = 1
    mod = 998244353
    right = 0
    while i * i <= n:
        left = n // i
        right = n // (i + 1) + 1
        res = (res + (left - right + 1) * i % mod) % mod
        i += 1
    for i in range(1, right):
        res = (res + n // i) % mod
    return res


if __name__ == '__main__':
    print(work(5))
    print(work(10))
