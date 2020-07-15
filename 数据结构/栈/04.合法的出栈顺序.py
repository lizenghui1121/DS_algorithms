"""
1到n的数字序列，入栈，每个数字入栈后，即可出栈，也可在栈中停留，求该数字序列的出栈序列是否合法。
@Author: Li Zenghui
@Date: 2020-03-21 21:19
"""
from queue_and_stack import MyStack


def check_is_valid_order(arr):
    s = MyStack()
    for i in range(1, len(arr)+1):
        s.push(i)
        while not s.is_empty() and arr[0] == s.top():
            s.pop()
            arr.pop(0)
    if not s.is_empty():
        return False
    return True


# 直接用列表当栈用
def check_is_valid_order_2(arr):
    s = []
    for i in range(1, len(arr)+1):
        s.append(i)
        while s and arr[0] == s[-1]:
            s.pop()
            arr.pop(0)
    if s:
        return False
    return True


if __name__ == '__main__':
    print(check_is_valid_order([3, 2, 5, 4, 1]))
    print(check_is_valid_order([3, 1, 2, 4, 5]))
    print(check_is_valid_order_2([3, 2, 5, 4, 1]))
    print(check_is_valid_order_2([3, 1, 2, 4, 5]))

