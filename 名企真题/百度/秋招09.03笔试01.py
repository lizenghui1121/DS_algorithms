"""
演员角色分配，贪心
@Author: Li Zenghui
@Date: 2020-09-04 18:50
"""

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    res = [-1] * n
    ta = list(zip(a, [i for i in range(n)]))
    ta.sort(reverse=True)
    tb = list(zip(b, [j for j in range(m)]))
    tb.sort(reverse=True)

    j = 0
    for x, idx in ta:
        if x > tb[j][0]:
            continue
        else:
            res[idx] = tb[j][1] + 1
            j += 1
    print(" ".join(map(str, res)))
