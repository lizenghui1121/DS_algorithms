"""

@Author: Li Zenghui
@Date: 2020-04-08 20:43
"""


def get_res(n, m, a, b):
    if b > m:
        return n if n >= a else 0
    else:
        return min(b * n // a, m)


t = int(input())

for i in range(t):
    n, m, a, b = map(int, input().split(" "))
    print(get_res(n, m, a, b))
