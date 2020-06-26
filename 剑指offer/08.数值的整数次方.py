"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
@Author: Li Zenghui
@Date: 2020-03-03 15:08
"""

class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        e = abs(exponent)
        res = 1
        while e > 0:
            if e & 1 == 1:
                res = res * base
            base = base * base
            e >>= 1
        return res if exponent > 0 else 1 / res


if __name__ == '__main__':
    s = Solution()
    print(s.Power(2, 3))
