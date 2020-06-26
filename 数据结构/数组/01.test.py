"""

@Author: Li Zenghui
@Date: 2020-03-25 20:03
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        s = set(numbers)
        flag = 0
        length = len(numbers)
        for num in s:
            if numbers.count(num) > length/2:
                return num
                flag = 1
                break
        if not flag:
            return 0

    def MoreThanHalfNum_Solution_2(self, numbers):
        num = numbers[0]
        length = len(numbers)
        count = 1
        for i in range(1, len(numbers)):
            if numbers[i] != num:
                count -= 1
            else:
                count += 1
            if count == 0:
                num = numbers[i]
                count = 1
        count = 0
        for i in range(length):
            if num == numbers[i]:
                count += 1

        return num if count > length/2 else 0

    def MoreThanHalfNum_Solution_3(self, numbers):
        length = len(numbers)
        nums = sorted(numbers)
        if nums.count(nums[length/2]) > length/2:
            return nums[length/2]
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1,2,5,6,3,4,2,2]))
    print(s.MoreThanHalfNum_Solution_2([1,2,2,2,4,2,2]))