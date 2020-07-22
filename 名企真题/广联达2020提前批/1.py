"""

@Author: Li Zenghui
@Date: 2020-07-22 22:16
"""
import collections
n = int(input())
nums = list(map(int, input().split()))
dic = collections.defaultdict(int)

for side in nums:
    dic[side] += 1

side_list = sorted(dic.keys(), reverse=True)
res = 1
i = 0
flag = False
for side in side_list:
    if i == 2:
        break
    if i == 0 and dic[side] >= 4:
        flag = True
        res = side * side
        break
    if dic[side] >= 2:
        res = res*side
        i += 1
if flag:
    print(res)
elif i < 2:
    print(-1)
else:
    print(res)