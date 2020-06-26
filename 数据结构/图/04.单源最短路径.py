"""

@Author: Li Zenghui
@Date: 2020-04-22 20:53
"""
V= 4
used = [False for i in range(4)]
distance = [float('inf') for i in range(4)]
cost = [[float('inf') for i in range(V)] for j in range(4)]


def dijkstra(s):
    distance[s] = 0
    while True:
        # v在这里相当于是一个哨兵，对包含起点s做统一处理！
        v = -1
        # 从未使用过的顶点中选择一个距离最小的顶点
        for u in range(V):
            if not used[u] and (v == -1 or distance[u] < distance[v]):
                v = u
        if v == -1:
            # 说明所有顶点都维护到S中了！
            break

        # 将选定的顶点加入到S中, 同时进行距离更新
        used[v] = True
        # 更新U中各个顶点到起点s的距离。之所以更新U中顶点的距离，是由于上一步中确定了k是求出最短路径的顶点，从而可以利用k来更新其它顶点的距离；例如，(s,v)的距离可能大于(s,k)+(k,v)的距离。
        for u in range(V):
            distance[u] = min(distance[u], distance[v] + cost[v][u])


if __name__ == '__main__':
    for _ in range(5):
        v, u, w = list(map(int, input().split()))
        cost[v][u] = w
    s = int(input('请输入一个起始点：'))
    dijkstra(s)
    print(distance)
