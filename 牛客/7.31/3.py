"""

@Author: Li Zenghui
@Date: 2020-08-01 21:01
"""


class Solution:
    def solve(self, n, x, a):
        a.sort(reverse=True)
        if x > a[0]:
            return 0
        pre_arr = [0]
        for i in range(1, n+1):
            pre_arr.append(pre_arr[-1] + a[i-1])
        print(pre_arr)
        ans = 0
        for i in range(1, len(pre_arr)):
            if pre_arr[i] / i >= x:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solve(3, 7, [9, 4, 9]))
    print(s.solve(2, 5, [4, 3]))
