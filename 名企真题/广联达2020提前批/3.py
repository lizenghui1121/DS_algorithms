"""

@Author: Li Zenghui
@Date: 2020-07-22 22:17
"""
"""

@Author: Li Zenghui
@Date: 2020-07-22 15:43
"""
# n 数量
n, y = map(int, input().split())

x_hp = []
res = 0
for i in range(n):
    x_hp.append(list(map(int, input().split())))

x_hp.sort(key=lambda x: x[1], reverse=True)
x_up = sorted(x_hp, key=lambda x: x[0])

x_max = x_up[-1][0]
x_min = x_up[0][0]
# y 很大
if x_hp[0][0] - y <= x_min and x_hp[0][0] + y >= x_max:
    res = x_hp[0][1]
    print(res)
else:
    while x_up:
        x_min = x_up[0][0]
        res += x_up[0][1]
        temp = x_up[0][1]
        for i in range(len(x_up)):
            if x_up[i][0] <= x_min+2*y:
                x_up[i][1] -= temp
            else:
                break
        while x_up and x_up[0][1] <= 0:
            x_up.pop(0)
    print(res)