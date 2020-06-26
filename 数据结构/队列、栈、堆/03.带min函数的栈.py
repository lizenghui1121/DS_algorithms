"""

@Author: Li Zenghui
@Date: 2020-03-21 21:06
"""


class MinStack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, n):
        if not self.min_stack:
            self.min_stack.append(n)
            self.items.append(n)
        elif n < self.items[-1]:
            self.min_stack.append(n)
            self.items.append(n)
        else:
            self.min_stack.append(self.min_stack[-1])
            self.items.append(n)

    def pop(self):
        if not self.items:
            return None
        self.min_stack.pop()
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def get_min_stack(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


if __name__ == '__main__':
    s = min_stackStack()
    s.push(1)
    s.push(-2)
    s.push(4)
    s.push(-5)
    s.push(3)
    print(s.get_min_stack())
    s.pop()
    s.pop()
    print(s.get_min_stack())
    print(s.top())
