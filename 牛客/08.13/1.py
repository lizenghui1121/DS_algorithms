"""

@Author: Li Zenghui
@Date: 2020-08-13 21:01
"""


#
#
# @param str string字符串 初始字符串
# @return string字符串
#
class Solution:
    def solve(self, str):
        sta = []
        for c in str:
            sta.append(c)
            while len(sta) > 1:
                if sta[-2] == "0" and sta[-1] == "0":
                    sta.pop()
                    sta.pop()
                    sta.append("1")
                elif sta[-2] == "1" and sta[-1] == "1":
                    sta.pop()
                    sta.pop()
                else:
                    break
        return "".join(sta)


if __name__ == '__main__':
    s = Solution()
    print(s.solve("00110001"))
    l = []
    l.append("")
    print(len(l))
