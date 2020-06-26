"""
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
@Author: Li Zenghui
@Date: 2020-02-29 21:19
"""
num = int(input())
count = 0
while num/2 != 0:
    if num % 2 == 1:
        count += 1
    num = num // 2
    print(num)
print(count)
print(1/2)
# print(bin(int(input())).count('1'))
# print(bin(3))