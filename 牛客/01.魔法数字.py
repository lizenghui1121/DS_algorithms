"""

@Author: Li Zenghui
@Date: 2020-07-09 21:08
"""


class Solution:
    def solve(self, n, m):
        dis = [-1] * 2100
        q = []
        q.append(n)
        while q:
            x = q.pop(0)
            if x == m:
                return dis[m]+1
            if x+1 <= m and dis[x+1] == -1:
                dis[x+1] = dis[x] + 1
                q.append(x+1)
            if x-1 >= 1 and dis[x-1] == -1:
                dis[x-1] = dis[x] + 1
                q.append(x-1)
            if x**2 <= m+m-n and dis[x**2] == -1:
                dis[x**2] = dis[x] + 1
                q.append(x**2)


if __name__ == '__main__':
    s = Solution()
    print(s.solve(6, 100))
