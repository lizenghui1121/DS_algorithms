"""

@Author: Li Zenghui
@Date: 2020-03-02 20:01
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        col = len(array[0])
        row = len(array)
        i = 0
        j = col -1
        while i <row and j >= 0:# write code here
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    target = 5
    test_array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(s.Find(target, test_array))
