"""

@Author: Li Zenghui
@Date: 2020-07-23 21:24
"""


class Solution:
    def solve(self, x):
        i = 0
        m = -1
        while m != x and i < pow(2, 16):
            m = i * i % 1000
            i += 1
        if m == x:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.solve(23))
