"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
@Author: Li Zenghui
@Date: 2020-03-03 14:01
"""


class Solution:
    def NumberOf1(self, n):
        s = int(n)  # write code here
        if n < 0:
            n = n & 0xffffffff
        print(n)
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-4))
