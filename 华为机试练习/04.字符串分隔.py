"""
连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
@Author: Li Zenghui
@Date: 2020-02-28 19:33
"""

s1 = input()
s2 = input()


def partition(s):
    length = len(s)
    if length <= 8:
        s = s + (8-length) * '0'
        print(s)
    else:
        mod = length % 8
        if mod != 0:
            s = s + (8-mod) * '0'
        num = int(len(s)/8)
        for i in range(num):
            index = 8 * i
            print(s[index:index+8])


# 递归解法
# def printStr(string):
#     if len(string) <= 8:
#         print(string + "0" * (8 - len(string)))
#     else:
#         while len(string) > 8:
#             print(string[:8])
#             string = string[8:]
#         print(string + "0" * (8 - len(string)))
# a=input()
# b=input()
# printStr(a)
# printStr(b)

partition(s1)
partition(s2)
