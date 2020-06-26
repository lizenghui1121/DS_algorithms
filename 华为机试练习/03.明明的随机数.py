"""
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
对于其中重复的数字，只保留一个，把其余相同的数去掉，不
同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
Input Param
n               输入随机数的个数
inputArray      n个随机整数组成的数组

Return Value
OutputArray    输出处理后的随机整数
@Author: Li Zenghui
@Date: 2020-02-27 21:08
"""
# n = int(input())
# result = []
# arr1 = []
# for i in range(n):
#     arr1.append(int(input()))
# result.extend(sorted(list(set(arr1))))
# m = int(input())
# arr1 = []
# for i in range(m):
#     arr1.append(int(input()))
# result.extend(sorted(list(set(arr1))))
# for i in result:
#     print(i)

while True:
    a, res = int(input()), set()
    for i in range(a):
        res.add(int(input()))
    for i in sorted(res):
        print(i)
