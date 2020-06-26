"""

@Author: Li Zenghui
@Date: 2020-04-05 16:40
"""


def Add(num1, num2):
    # write code here
    while num2 != 0:
        temp = num1 ^ num2
        num2 = (num1 & num2) << 1
        num1 = temp
    return num1


if __name__ == '__main__':
    print(Add(10, 7))
    print(4 & 3)
