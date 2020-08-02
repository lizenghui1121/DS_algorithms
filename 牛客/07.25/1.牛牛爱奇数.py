"""

@Author: Li Zenghui
@Date: 2020-07-25 22:56
"""


class Solution:
    def solve(self , n , a ):
        # write code here
        res=0
        tempres=[]
        s = set()
        for num in a:
            if num % 2 == 0:
                if num not in s:
                    tempres.append(num)
                    s.add(num)
                else:
                    continue
        tempres.sort(reverse=True)
        for index, item in enumerate(tempres):
            s.remove(item)
            while item % 2 == 0 and item not in s:
                res += 1
                item = item // 2
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solve(3, [3, 2, 3]))
    print(6 // 0)
