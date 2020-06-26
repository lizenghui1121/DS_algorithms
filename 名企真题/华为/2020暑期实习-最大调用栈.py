"""

@Author: Li Zenghui
@Date: 2020-04-15 17:20
"""
class Node:
    def __init__(self, label, weight, nbrs=[]):
        self.label = label
        self.weight = weight
        self.nbrs = nbrs
def result():
    def dfs(node, pathvalue, path, visit):
        visit[node] = 0
        pathvalue += node.weight
        path.append(node)
        count = 0
        for nbr in node.nbrs:
            if visit[nodes[nbr - 1].label] == 1:
                count += 1
        if not nbrs or count == len(node.nbrs):
            res.append(pathvalue)
        for nbr in node.nbrs:
            if visit[nodes[nbr - 1].label] == -1 and visit[nodes[nbr - 1].label] != 0:
                dfs(nodes[nbr - 1], pathvalue, path, visit)
            if visit[nodes[nbr - 1].label] == 0:
                digui[0] = True
        pathvalue -= node.weight
        path.pop()
        visit[node.label] == 1
    group_info = list(map(int, input().split()))
    f_num = group_info[1:]
    nodes = []
    no_weight = False
    for i in range(group_info[0]):
        node_infos = list(map(int, input().split()))
        if len(node_infos) < 2 or len(node_infos) < 2+f_num[i]:
            no_weight = True
            break
        label = node_infos[0]
        weight = node_infos[1]
        nbrs = node_infos[2:]
        nodes.append(Node(label, weight, nbrs))

    if no_weight:
        return 'NA'
    visit = {item.label: -1 for item in nodes}
    path = []
    pathvalue = 0
    res = []
    digui = [False]
    for node in nodes:
        if visit[node.label] == -1:
            dfs(node, pathvalue, path, visit)
    if digui[0]:
        return 'R'
    else:
        return max(res)

print(result())





