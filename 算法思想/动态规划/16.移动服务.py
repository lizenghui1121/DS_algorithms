"""

@Author: Li Zenghui
@Date: 2020-08-17 20:32
"""

m, n = map(int, input().split())

w = [[0] + list(map(int, input().split())) for _ in range(m)]
w = [[0] * (m+1)] + w
print(w)
p = [3] + list(map(int, input().split()))
print(p)
f = [[[float('inf')]*210 for _ in range(210)] for i in range(210)]
# print(f)
f[0][1][2] = 0

for i in range(n):
    for x in range(1, m+1):
        for y in range(1, m+1):
            z, u, v = p[i], p[i+1], f[i][x][y]
            if x == y or y == z or x == z:
                continue
            f[i+1][x][y] = min(f[i+1][x][y], v + w[z][u])
            f[i+1][z][y] = min(f[i+1][z][y], v + w[x][u])
            f[i+1][x][z] = min(f[i+1][x][z], v + w[y][u])

ans = float('inf')
for x in range(1, m+1):
    for y in range(1, m+1):
        z = p[n]
        if x == y or y == z or x == z:
            continue
        ans = min(ans, f[n][x][y])
print(ans)