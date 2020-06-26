"""

@Author: Li Zenghui
@Date: 2020-04-04 21:57
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        for i in range(1, tsum//2+2):
            count = i
            path = [i]
            for j in range(i+1, tsum//2+2):
                path.append(j)
                count += j
                if count == tsum:
                    res.append(path)
                if count >= tsum:
                    break
        return res

    def FindContinuousSequence2(self, tsum):
        # write code here
        arr = [i for i in range(tsum // 2 + 3)]
        print(arr)
        left = 1
        right = 2
        res = []
        if tsum < 3:
            return []
        while left < right:
            if sum(arr[left:right + 1]) == tsum:
                res.append(arr[left:right + 1])
                left += 1
            elif sum(arr[left:right + 1]) < tsum:
                right += 1
            else:
                left += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.FindContinuousSequence2(9))
