"""

@Author: Li Zenghui
@Date: 2020-08-08 16:38
"""


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(12, 6))
print(lcm(12, 6))
print(gcd(21, 12))
print(gcd(15, 35))