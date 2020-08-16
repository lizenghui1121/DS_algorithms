"""

@Author: Li Zenghui
@Date: 2020-08-15 20:32
"""


class UnionFind:
    def __init__(self, n):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        while x != self.f[x]:
            self.f[x] = self.f[self.f[x]]
            x = self.f[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.f[x_root] = y_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        flag = True
        uf = UnionFind(n)
        not_equals = []
        for i in range(n):
            x, y, e = map(int, input().split())
            if e == 1:
                uf.union(x, y)
            else:
                not_equals.append([x, y])
        for x, y in not_equals:
            if uf.connected(x, y):
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")