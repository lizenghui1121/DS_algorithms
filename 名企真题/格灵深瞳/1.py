"""

@Author: Li Zenghui
@Date: 2020-06-03 14:38
"""
import math

k = int(input())
data = []
for i in range(k):
    z, p = map(int, input().split())
    data.append([z, p])

res = 1

for item in data:
    if item[0] == 1:
        res = res+item[1]
    elif item[0] == 2:
        res = res * item[1]
    else:
        res = math.ceil(res/item[1])
print(res)
