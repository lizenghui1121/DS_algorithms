"""

@Author: Li Zenghui
@Date: 2020-04-03 21:38
"""


class Solution:

    def InversePairs(self, data):
        # write code here
        def merge(arr_left, arr_right, result):
            res = []
            while arr_left and arr_right:
                if arr_left[0] > arr_right[0]:
                    res.append(arr_right.pop(0))
                    result[0] += len(arr_left)-l
                else:
                    res.append(arr_left.pop(0))
            while arr_left:
                res.append(arr_left.pop(0))
            while arr_right:
                res.append((arr_right.pop(0)))
            return res

        def merge_sort(arr, result):
            if len(arr) < 2:
                return arr
            middle = len(arr) // 2
            sub_left, sub_right = arr[0:middle], arr[middle:]
            return merge(merge_sort(sub_left, result), merge_sort(sub_right, result), result)

        result = [0]
        s = merge_sort(data, result)
        return result[0]


if __name__ == '__main__':
    s = Solution()
    print(s.InversePairs([4, 3, 1, 2, 6]))
