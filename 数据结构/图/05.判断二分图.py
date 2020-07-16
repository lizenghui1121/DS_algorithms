"""
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

@Author: Li Zenghui
@Date: 2020-07-16 10:36
"""

# dfs
def isBipartite1(graph):
    n = len(graph)
    color = [0] * n
    valid = [True]

    def dfs(node, cur):
        color[node] = cur
        color_next = 2 if cur == 1 else 1
        for nbr in graph[node]:
            if color[nbr] == 0:
                dfs(nbr, color_next)
                if not valid[0]:
                    return
            elif color[nbr] != color_next:
                valid[0] = False
                return

    for i in range(n):
        if color[i] == 0:
            dfs(i, 1)
            if not valid[0]:
                break
    return valid[0]


# bfs
def isBipartite2(graph):
    import collections
    n = len(graph)
    color = [0] * n

    q = collections.deque()
    for i in range(n):
        if color[i] == 0:
            q.append(i)
            color[i] = 1
            while q:
                node = q.popleft()
                color_next = 2 if color[node] == 1 else 1
                for nbr in graph[node]:
                    if color[nbr] == 0:
                        q.append(nbr)
                        color[nbr] = color_next
                    elif color[nbr] != color_next:
                        return False
    return True


if __name__ == '__main__':
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(isBipartite1(graph))
    print(isBipartite2(graph))
