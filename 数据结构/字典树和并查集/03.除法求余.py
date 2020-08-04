"""
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， 
k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

基于上述例子，输入如下：
equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

@Author: Li Zenghui
@Date: 2020-08-04 10:41
"""
from typing import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        dic = {}
        for i in range(len(equations)):
            n1 = equations[i][0]
            n2 = equations[i][1]
            val = values[i]
            dic[n1] = 1
            dic[n2] = 1
            uf.union(n1, n2, val)

        res = [-1.0] * len(queries)
        for i in range(len(queries)):
            q = queries[i]
            if q[0] not in dic or q[1] not in dic:
                res[i] = -1.0
            else:
                res[i] = uf.connected(q[0], q[1])
        return res


class UnionFind:
    def __init__(self):
        self.f = {}
        self.weight = {}

    def find(self, x):
        self.f.setdefault(x, x)
        self.weight.setdefault(x, 1.0)
        if x != self.f[x]:
            origin = self.f[x]
            self.f[x] = self.find(self.f[x])
            self.weight[x] *= self.weight[origin]
        return self.f[x]

    def union(self, x, y, val):
        root_x = self.find(x)
        root_y = self.find(y)
        self.f[root_x] = root_y
        self.weight[root_x] = self.weight[y] * val / self.weight[x]

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return self.weight[x] / self.weight[y]
        else:
            return -1.0


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    s = Solution()
    print(s.calcEquation(equations, values, queries))
