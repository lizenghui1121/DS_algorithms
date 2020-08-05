"""

@Author: Li Zenghui
@Date: 2020-08-05 11:42
"""

nums = [1, 2, 3, 4, 5]
pre_sum = [0]
for num in nums:
    pre_sum.append(pre_sum[-1] + num)
print(pre_sum)

print(pre_sum[4]-pre_sum[1])
print(pre_sum[3]-pre_sum[2])
