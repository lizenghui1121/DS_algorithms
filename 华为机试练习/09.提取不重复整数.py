"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
@Author: Li Zenghui
@Date: 2020-02-29 13:32
"""

num = input()
s = num[::-1]
res = ''
d = set()
for i in s:
    if i not in d:
        d.add(i)
        res += i
print(res)

# 2.简洁做法
# result = ""
# for i in input()[::-1]
#     if i not in result:
#         result += i
# print(result)
