"""
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述:
输出输入字符串中含有该字符的个数。
@Author: Li Zenghui
@Date: 2020-02-27 21:01
"""
s = input().lower()
key = input().lower()
# 1.常规思路
# count = 0
# for i in s:
#     if i == key:
#         count += 1
# print(count)

# 便捷方法
print(s.count(key))
