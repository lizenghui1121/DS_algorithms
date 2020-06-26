"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
@Author: Li Zenghui
@Date: 2020-02-29 12:26
"""

n = float(input())
m = int(n)
c = n-m
if c >= 0.5:
    print(m+1)
else:
    print(m)

# print(round(float(input()) + 0.001))