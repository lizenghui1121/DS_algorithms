"""
已知n个课程，0到n-1,课程之间有依赖关系，例如希望完成A课程，需要先王城B课程。已知n个课程的依赖关系，求是否能将n个课程全部完成。

思路：
转换为图是否是有向无环图。有环的话，一定不能完成。
@Author: Li Zenghui
@Date: 2020-03-22 21:29
"""


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbor = []


# 方法1：深度优先搜索---如果正在搜索某一顶点(还未退出该顶点的递归深度优先搜索)，又回到了该顶点，即证明图有环
def can_finish(num, arr):
    visit = [-1 for i in range(num)]
    graph = [GraphNode(i) for i in range(num)]

    for item in arr:
        begin_node = graph[item[1]]
        end_node = graph[item[0]]
        begin_node.neighbor.append(end_node)

    for i in range(num):
        if visit[i] == -1 and not dfs_graph(graph[i], visit):
            return False
    return True


def dfs_graph(node, visit):
    visit[node.label] = 0
    for neighbor in node.neighbor:
        if visit[neighbor.label] == -1:
            if not dfs_graph(neighbor, visit):
                return False
        elif visit[neighbor.label] == 0:
            return False
    visit[node.label] = 1
    return True


# 方法2：拓扑排序，宽度优先搜索，只将入度为0的顶点加入队列。当完成一个顶点的搜索，它指向的所有顶点的入度都减1.
# 若此时，某结点入度为0，则添加至队列，若完成宽度搜索后，所有结点的度都为0，则说明图无环，否则有环。
def can_finish_two(num, arr):
    degree = [0 for i in range(num)]
    graph = [GraphNode(i) for i in range(num)]

    for item in arr:
        begin_node = graph[item[1]]
        end_node = graph[item[0]]
        begin_node.neighbor.append(end_node)
        degree[end_node.label] += 1
    q = []
    for i in range(num):
        if degree[graph[i].label] == 0:
            q.append(graph[i])
            break
    while q:
        temp_node = q.pop(0)
        for neighbor in temp_node.neighbor:
            degree[neighbor.label] -= 1
            if degree[neighbor.label] == 0:
                q.append(neighbor)
    for i in degree:
        if i != 0:
            return False
    return True


if __name__ == '__main__':
    print(can_finish(2, [[0, 1], [1, 0]]))
    print(can_finish_two(3, [[1, 0], [2, 0], [1, 2]]))
