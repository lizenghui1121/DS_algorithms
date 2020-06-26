"""

@Author: Li Zenghui
@Date: 2020-04-29 19:23
"""

k = int(input())
n = int(input())
r = int(input())
graph = [{} for node in range(1, n+1)]
for i in range(r):
    s, d, l, t = map(int, input().split())
    if d-1 not in graph[s-1]:
        graph[s-1][d-1] = [[l, t]]
    else:
        graph[s - 1][d - 1].append([l, t])

cost = 0
path_len = 0
path = []
res = []
visit = [0 for i in range(n)]

def dfs(node,path_len, cost, res):
    if node == n-1:
        res.append(path_len)
        return
    path.append(node)
    visit[node] = 1
    for nbr in graph[node]:
        if visit[nbr] == 1:
            continue
        for edge in graph[node][nbr]:
            if k - cost >= edge[1]:
                cost += edge[1]
                path_len += edge[0]
                dfs(nbr,path_len, cost, res)
                path_len -= edge[0]
                cost -= edge[1]
            else:
                continue
    path.pop()
    visit[node] = 0

dfs(0,path_len, cost, res)
if not res:
    print(-1)
else:
    print(min(res))