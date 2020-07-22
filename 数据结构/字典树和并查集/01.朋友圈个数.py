"""
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，
那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

@Author: Li Zenghui
@Date: 2020-03-31 15:31
"""


def findCircleNum(M):
    f = {}
    s = {}
    count = len(M)

    def find(x):
        f.setdefault(x, x)
        # 路径压缩
        while x != f[x]:
            f[x] = f[f[x]]
            x = f[x]
        return x
        # if x != f[x]:
        #     f[x] = find(f[x])
        # return f[x]

    def union(x, y):
        nonlocal count
        x_father = find(x)
        y_father = find(y)
        if x_father == y_father:
            return
        else:
            # 将小树的根节点连接到大树的根节点
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j] == 1:
                union(i, j)
    return count


if __name__ == '__main__':
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print(findCircleNum(M))
