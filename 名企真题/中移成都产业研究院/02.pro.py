"""

@Author: Li Zenghui
@Date: 2020-03-17 20:10
"""

n, k = map(int, input().split())
price = sorted(list(map(int, input().split())))

cost = 0
for i in range(len(price)):
    cost += price[i]
    if cost > k:
        print(i)
        break
