"""

@Author: Li Zenghui
@Date: 2020-08-24 22:10
"""

n = int(input())

cow = []

for _ in range(n):
    w, s = map(int, input().split())
    cow.append((s + w, w))

cow.sort()
print(cow)
res = float('-inf')
sumv = 0
for i in range(n):
    t, w = cow[i]
    res = max(res, sumv - t + w)
    sumv += w
print(res)
