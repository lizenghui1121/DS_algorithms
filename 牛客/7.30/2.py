"""

@Author: Li Zenghui
@Date: 2020-07-30 20:59
"""


#
# 两个数表示答案
# @param n int整型 一次运输的冰激凌数量
# @param m int整型 总冰激凌数
# @param t int整型 一次运输的时间
# @param c int整型一维数组 表示每个冰激凌制作好时间<1e4
# @return int整型一维数组
#
class Solution:
    def icecream(self, n, m, t, c):
        c.sort()
        remain = m % n
        if not remain:
            remain = n
        ans = -t
        for i in range(remain - 1, m, n):
            ans += t
            ans = max(ans, c[i])
            ans += t
        return [ans, m // n + (m % n != 0)]


if __name__ == '__main__':
    s = Solution()
    print(s.icecream(2, 3, 10, [10, 30, 40]))
