"""

@Author: Li Zenghui
@Date: 2020-03-22 20:42
"""


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbor = []

# 邻接矩阵,一般表示稠密图
g = [[0 for i in range(5)] for i in range(5)]
g[0][2] = 1
g[0][4] = 1
g[1][0] = 1
g[1][2] = 1
g[2][3] = 1
g[3][4] = 1
g[4][3] = 1
for row in g:
    print(row, end="\n")

if __name__ == '__main__':
    g1 = GraphNode(0)
    g2 = GraphNode(1)
    g3 = GraphNode(2)
    g4 = GraphNode(3)
    g5 = GraphNode(4)
    g1.neighbor.append(g2.label)
    g1.neighbor.append(g3.label)
    print(g1.neighbor)
