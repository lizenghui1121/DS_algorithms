"""
使用队列实现栈
@Author: Li Zenghui
@Date: 2020-03-21 20:54
"""

class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []


class MyStack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []


