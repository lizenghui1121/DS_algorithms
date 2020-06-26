"""
编写一个函数，计算字符串中含有的不同字符的个数。
字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。
@Author: Li Zenghui
@Date: 2020-02-29 13:49
"""
# s = input()
# res = ''
# for i in s:
#     if chr(0) <= i <= chr(127):
#         if i not in res:
#             res += i
# print(len(res))

# 一行代码解法
print(len(set([i for i in input() if ord(i) in range(128)])))

