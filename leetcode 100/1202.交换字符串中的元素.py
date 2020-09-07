"""

@Author: Li Zenghui
@Date: 2020-08-31 21:56
"""

import collections


def smallestStringWithSwaps(s, pairs):
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    p = {i: i for i in range(len(s))}  # 初始化并查集

    def f(x):
        if x != p[x]:
            p[x] = f(p[x])
        return p[x]

    for i, j in pairs:
        p[f(i)] = j
    print(p)
    # 合并可交换位置
    d = collections.defaultdict(list)
    for i, j in enumerate(map(f, p)):
        print(i, j)
        d[j].append(i)
    print(d)
    # 排序
    ans = list(s)
    for q in d.values():
        t = sorted(ans[i] for i in q)
        for i, c in zip(sorted(q), t):
            ans[i] = c
    return ''.join(ans)


if __name__ == '__main__':
    s = "dcabfge"
    pairs = [[0, 3], [1, 2], [0, 2], [4, 6]]
    print(smallestStringWithSwaps(s, pairs))
