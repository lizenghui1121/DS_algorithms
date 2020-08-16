"""

@Author: Li Zenghui
@Date: 2020-08-15 23:40
"""


class Solution:
    def solve(self, n, x, Edge):
        import collections
        def dfs(node, dist):
            qe = [node]
            dist[node] = 0
            while len(qe) > 0:
                u = qe.pop(0)
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        qe.append(v)

        graph = collections.defaultdict(list)
        for edge in Edge:
            graph[edge.x].append(edge.y)
            graph[edge.y].append(edge.x)
        d1 = [-1] * (n + 1)
        dx = [-1] * (n + 1)
        dfs(1, d1)
        dfs(x, dx)
        ans = 0
        for v in range(1, n + 1):
            if d1[v] > dx[v]:
                ans = max(ans, d1[v] + 1)
        return ans
