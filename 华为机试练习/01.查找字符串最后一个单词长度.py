"""
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。
@Author: Li Zenghui
@Date: 2020-02-27 20:49
"""
s = input()
print(len(s.split(' ')[-1]))
