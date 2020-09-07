"""

@Author: Li Zenghui
@Date: 2020-09-07 15:36
"""

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    ans = 0
    for num in a:
        ans += num
        if ans <= m:
            cnt += 1
    print(cnt)