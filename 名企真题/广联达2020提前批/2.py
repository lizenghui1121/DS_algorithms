"""

@Author: Li Zenghui
@Date: 2020-07-22 22:16
"""

n = int(input())
nums = list(map(int, input().split()))

count = 0
temp = n
for i in range(n-1, -1, -1):
    if nums[i] == temp:
        count += 1
        temp = temp - 1
res = n - count
print(res)