"""
优质的奶牛，覆盖所有属性的奶牛
@Author: Li Zenghui
@Date: 2020-09-04 18:50
"""

import collections

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dic = collections.defaultdict(list)
    for i in range(m):
        k = int(input())
        for j in range(k):
            dic[k].append(list(map(int, input().split())))
    cnt = [0] * (n + 1)
    for key in dic:
        for l in dic[key]:
            cnt[l[0]] += 1
            cnt[l[1]+1] -= 1
    # 差分
    print(cnt)
    pre_sum = [0]
    for i in range(len(cnt)):
        pre_sum.append(pre_sum[-1] + cnt[i])
    # 前缀和
    # print(pre_sum)
    res = []
    for i in range(len(pre_sum)):
        if pre_sum[i] == m:
            res.append(i-1)
    # print(res)
    print(" ".join(map(str, res)))