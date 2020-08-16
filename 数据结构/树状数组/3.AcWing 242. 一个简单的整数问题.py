"""

@Author: Li Zenghui
@Date: 2020-08-16 09:46
"""


class FW:
    def __init__(self, n):
        self.a = [0]
        self.b = [0] * (n + 1)
        self.size = n

    def lowbit(self, x):
        return x & -x

    def update(self, i, k):
        while i <= self.size:
            self.b[i] += k
            i += self.lowbit(i)

    def ask(self, i):
        ans = self.a[i]
        while i > 0:
            ans += self.b[i]
            i -= self.lowbit(i)
        return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    n = len(A)
    fw = FW(n)
    fw.a.extend(A)
    print(fw.a)
    for _ in range(M):
        op = list(input().split())
        if op[0] == "Q":
            print(fw.ask(int(op[1])))
        if op[0] == "C":
            fw.update(int(op[1]), int(op[3]))
            fw.update(int(op[2]) + 1, -int(op[3]))
