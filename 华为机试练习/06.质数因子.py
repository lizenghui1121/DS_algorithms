"""
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格
@Author: Li Zenghui
@Date: 2020-02-29 12:10
"""
num = int(input())

i = 2
while num != 1:
    if num % i == 0:
        print(i, end=' ')
        num = num/i
    else:
        i += 1
