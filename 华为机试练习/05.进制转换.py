"""
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
@Author: Li Zenghui
@Date: 2020-02-29 11:39
"""

while True:
    try:
        print(int(input(), 8))
    except:
        break