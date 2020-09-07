"""

@Author: Li Zenghui
@Date: 2020-09-07 15:41
"""

n = int(input())

heights = list(map(int, input().split()))

max_height = 0
max_index_list = []
max_height_index = -1
for i in range(n):
    if heights[i] > max_height:
        max_index_list = [i]
        max_height = heights[i]
    elif heights[i] == max_height:
        max_index_list.append(i)

res = []
max_sum = 0
for max_index in max_index_list:
    sta1 = []
    ans = [0] * n
    for i in range(max_index + 1):
        while sta1 and heights[i] <= heights[sta1[-1]]:
            ans[sta1.pop()] = heights[i]
        sta1.append(i)
        ans[i] = heights[i]
    for i in range(max_index + 1, n):
        if sta1 and heights[i] > heights[sta1[-1]]:
            ans[i] = heights[sta1[-1]]
        else:
            sta1.append(i)
            ans[i] = heights[i]
    total = sum(ans)
    if total >= max_sum:
        max_sum = total
        res = ans.copy()
print(" ".join(map(str, res)))
