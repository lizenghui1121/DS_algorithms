"""

@Author: Li Zenghui
@Date: 2020-08-25 22:22
"""

import collections

n, m = map(int, input().split())

a = list(map(int, input().split()))
print(a)
s = [0]

for i in range(len(a)):
    s.append(s[-1] + a[i])
print(s)
q = collections.deque()

q.append(0)

res = float('-inf')
for i in range(0, len(a)):
    if i+1 - q[0] > m:
        q.popleft()
    res = max(res, s[i+1] - s[q[0]])
    print(q, res)
    while q and s[q[-1]] >= s[i+1]:
        q.pop()
    q.append(i+1)
print(res)
