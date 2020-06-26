"""
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
@Author: Li Zenghui
@Date: 2020-02-29 12:43
"""
num = int(input())

d = {}
for i in range(num):
    index, value = map(int, input().split(' '))
    if index not in d.keys():
        d[index] = value
    else:
        d[index] = d[index] + value
for i in sorted(d.keys()):
    print(str(i) + " " + str(d[i]))
# defaultdict解法
# from collections import defaultdict
# # while True:
# #     try:
# #
# #         a, dd = int(input()), defaultdict(int)
# #         for i in range(a):
# #             key, val = map(int, input().split())
# #             dd[key] += val
# #         for i in sorted(dd.keys()):
# #             print(str(i) + " " + str(dd[i]))
# #
# #
# #     except:
# #         break