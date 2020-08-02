"""

@Author: Li Zenghui
@Date: 2020-07-30 20:59
"""

#
# 输出序列的第n项
# @param n long长整型 序列的项数
# @param b long长整型 系数
# @param c long长整型 系数
# @return long长整型
#
class Solution:
    def nthElement(self , n , b , c ):
        mod = 10 ** 9 + 7
        a0 = 0
        a1 = 1
        for i in range(2, n+1):
            temp = b * a0 % mod
            a0 = c * a1 % mod
            cur = temp + a0 % mod
            a0 = a1
            a1 = cur
        return cur % mod


if __name__ == '__main__':
    s = Solution()
    print(s.nthElement(2, 1, 1))
    print(s.nthElement(5, 1, 2))