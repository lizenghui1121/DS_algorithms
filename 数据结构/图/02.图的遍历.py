"""

@Author: Li Zenghui
@Date: 2020-03-22 20:55
"""


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbor = []


def dfs_graph(node, visit):
    visit[node.label] = 1
    print(node.label)
    for j in node.neighbor:
        if visit[j.label] == 0:
            dfs_graph(j, visit)


def bfs_graph(node, visit):
    q = []
    q.append(node)
    visit[node.label] = 1
    while q:
        temp_node = q.pop(0)
        print(temp_node.label)
        for i in temp_node.neighbor:
            if visit[i.label] == 0:
                q.append(i)
                visit[i.label] = 1


if __name__ == '__main__':
    graph = []
    for i in range(5):
        g = GraphNode(i)
        graph.append(g)
    graph0 = GraphNode(0)
    g1 = GraphNode(1)
    g2 = GraphNode(2)
    g3 = GraphNode(3)
    g4 = GraphNode(4)
    graph[0].neighbor.append(graph[4])
    graph[0].neighbor.append(graph[2])
    graph[1].neighbor.append(graph[0])
    graph[1].neighbor.append(graph[2])
    graph[2].neighbor.append(graph[3])
    graph[3].neighbor.append(graph[4])
    graph[4].neighbor.append(graph[3])
    visited = [0 for i in range(len(graph))]

    # for i in range(5):
    #     if visited[i] == 0:
    #         dfs_graph(graph[i], visited)
    # print("------")
    for i in range(5):
        if visited[i] == 0:
            bfs_graph(graph[i], visited)


