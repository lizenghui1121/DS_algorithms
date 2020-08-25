"""

@Author: Li Zenghui
@Date: 2020-08-25 14:28
"""


def get_mod(x):
    return (x % 10 + 10) % 10


n, m = map(int, input().split())

a = []
s = [0]

for _ in range(n):
    a.append(int(input()))

a = a + a
for i in range(len(a)):
    s.append(s[-1] + a[i])
print(a)
print(len(s))
print(s)
lenv = len(a)

f = [[[float('inf')] * (m + 1) for _ in range(lenv + 1)] for _ in range(lenv + 1)]
g = [[[float('-inf')] * (m + 1) for _ in range(lenv + 1)] for _ in range(lenv + 1)]
# 枚举区间长度
for _len in range(1, n + 1):
    for i in range(0, lenv - _len + 2):
        r = i + _len - 1
        print(i, r)
        f[i][r][1] = get_mod(s[r] - s[i-1])
        g[i][r][1] = get_mod(s[r] - s[i-1])
        for k in range(2, m+1):
            for j in range(i + k - 2, r):
                f[i][r][k] = min(f[i][r][k], f[i][j][k - 1] * get_mod(s[r] - s[j]))
                g[i][r][k] = max(g[i][r][k], g[i][j][k - 1] * get_mod(s[r] - s[j]))

minv, maxv = float('inf'), float('-inf')
print(f)
print(g)
for i in range(1, n+1):
    minv = min(minv, f[i][i + n-1][m])
    maxv = max(maxv, g[i][i + n-1][m])

print(minv)
print(maxv)