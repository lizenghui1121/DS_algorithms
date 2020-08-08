"""

@Author: Li Zenghui
@Date: 2020-08-06 20:58
"""


#
#
# @param n int整型
# @param m int整型
# @param a int整型一维数组
# @return int整型
#
class Solution:
    def solve(self, n, m, a):
        i = 0
        j = 0
        res = 0
        cur_len = 0
        while j < len(a):
            cur = a[j]
            cur_len += 1
            if cur == 0:
                m -= 1
            if m == -1:
                res = max(res, cur_len - 1)
                while m < 0:
                    if a[i] == 0:
                        m += 1
                    cur_len -= 1
                    i += 1
            res = max(res, cur_len)
            j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solve(6,1, [1,0,0,1,1,1]))
