"""

@Author: Li Zenghui
@Date: 2020-04-05 16:16
"""


def LastRemaining_Solution(n, m):
    # write code here
    if n == 0:
        return -1
    q = [i for i in range(n)]
    print(q)
    while len(q) > 1:
        t = m
        while t > 1:
            q.append(q.pop(0))
            print(q)
            t -= 1
        q.pop(0)
    return q[0]


if __name__ == '__main__':
    print(LastRemaining_Solution(3, 2))
