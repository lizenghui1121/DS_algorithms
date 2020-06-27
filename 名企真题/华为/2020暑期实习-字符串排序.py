"""

@Author: Li Zenghui
@Date: 2020-04-29 19:04
"""

s = list(input())
res = [0]

def dfs(i):
    if i == len(s) - 1:
        res[0] += 1
        return
    dic = set()
    for j in range(i, len(s)):
        if s[j] in dic:
            continue
        dic.add(s[j])
        print(dic)
        s[j], s[i] = s[i], s[j]
        dfs(i + 1)
        s[j], s[i] = s[i], s[j]

dfs(0)
print(res[0])
