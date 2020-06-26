"""

@Author: Li Zenghui
@Date: 2020-04-29 19:04
"""

s = list(input())
res = [0]

def dfs(x):
    if x == len(s) - 1:
        res[0] += 1
        return
    dic = set()
    for i in range(x, len(s)):
        if s[i] in dic:
            continue
        dic.add(s[i])
        s[i], s[x] = s[x], s[i]
        dfs(x + 1)
        s[i], s[x] = s[x], s[i]

dfs(0)
print(res[0])
