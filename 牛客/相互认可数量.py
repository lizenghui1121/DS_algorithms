"""
求相互认可数量
@Author: Li Zenghui
@Date: 2020-08-09 08:27
"""
import collections


class UF:
    def __init__(self, M):
        self.f = {}
        self.count = 0

    def find(self, x):
        self.f.setdefault(x, x)
        while x != self.f[x]:
            if
            self.f[x] = self.f[self.f[x]]
            x = self.f[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        else:
            self.f[y_root] = x_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def f(edges):
    adj = collections.defaultdict(set)
    for start, end in edges:
        adj[start].add(end)
    print(adj)
    uf = UF()


if __name__ == '__main__':
    edges = [[1, 3], [2, 1], [3, 2], [3, 4], [4, 5], [5, 4]]
    print(f(edges))
