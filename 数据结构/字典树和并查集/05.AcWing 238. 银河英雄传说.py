"""

@Author: Li Zenghui
@Date: 2020-08-15 21:00
"""


class UnionFind:
    def __init__(self, n):
        self.f = [i for i in range(n)]
        self.size = [1] * n
        self.d = [0] * n

    def find(self, x):
        if x != self.f[x]:
            root = self.find(self.f[x])
            self.d[x] += self.d[self.f[x]]
            self.f[x] = root
        return self.f[x]

    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.f[x_root] = y_root
        self.d[x_root] = self.size[y_root]
        self.size[y_root] += self.size[x_root]


if __name__ == '__main__':

    T = int(input())
    uf = UnionFind(30010)
    for _ in range(T):
        command, x, y = input().split()
        x, y = int(x), int(y)
        if command == "M":
            uf.merge(x, y)
        else:
            if uf.find(x) == uf.find(y):
                print(abs(uf.d[x] - uf.d[y]) - 1)
            else:
                print(-1)