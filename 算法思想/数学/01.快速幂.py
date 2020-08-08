"""
// 求 m^k mod p，时间复杂度 O(logk)。
@Author: Li Zenghui
@Date: 2020-08-08 16:27
"""


def mul(m, k, p):
    res = 1 % p
    t = m
    while k:
        if k & 1:
            res = res * t % p
        t = t * t % p
        k >>= 1
    return res


print(mul(2, 10, 100000000))