"""

@Author: Li Zenghui
@Date: 2020-04-05 22:14
"""


class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        self.nums.append(num)
        self.nums.sort()
        # write code here

    def GetMedian(self, data):
        # write code here
        length = len(self.nums)
        if length % 2 == 0:
            return (self.nums[length//2] + self.nums[length//2-1])/2
        else:
            return self.nums[length//2]


if __name__ == '__main__':
    s = Solution()
    s.Insert(5)
    print(s.GetMedian(1))
    s.Insert(2)
    print(s.GetMedian(1))
    s.Insert(3)
    print(s.GetMedian(1))
    s.Insert(4)
    print(s.GetMedian(1))
    s.Insert(1)
    print(s.GetMedian(1))
    s.Insert(6)
    print(s.GetMedian(1))
    s.Insert(7)
    print(s.GetMedian(1))
    s.Insert(0)
    print(s.GetMedian(1))
    s.Insert(8)
    print(s.GetMedian(1))
