"""

@Author: Li Zenghui
@Date: 2020-04-14 10:31
"""


def fun1(p, q):
    temp = p % q
    while temp != 0:
        p = q
        q = temp
        temp = p % q
    return q


def fun2(p, q):
    s = p * q
    while p%q!=0:
        p, q = q, (p%q)
    return q, int(s/q)

print(fun1(12, 6))
print(fun1(6, 12))
print(fun2(24, 18))
