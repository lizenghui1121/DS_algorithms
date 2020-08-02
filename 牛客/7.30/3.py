"""

@Author: Li Zenghui
@Date: 2020-07-30 21:00
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def solve(self, n, Edge, f):
        adj = [[] for _ in range(n)]
        for point in Edge:
            adj[point.x - 1].append(point.y - 1)
            adj[point.y - 1].append(point.x - 1)
        visited = [False for _ in range(n)]
        res = 0

        def dfs(node, rest, visited):
            nonlocal res
            visited[node] = True
            if f[node] > rest:
                return
            rest -= f[node]
            flag = True
            for nbr in adj[node]:
                if not visited[nbr]:
                    flag = False
                    dfs(nbr, rest, visited)
            if flag and rest >= 0:
                res += 1
            rest += f[node]

        dfs(0, 2, visited)
        return res


if __name__ == '__main__':
    s = Solution()
    edge = [(7, 2), (6, 1), (5, 2), (1, 2), (4, 6), (6, 3)]
    edges = []
    for x, y in edge:
        edges.append(Point(x, y))
    print(s.solve(7, edges, [0, 0, 1, 0, 1, 0, 0]))
