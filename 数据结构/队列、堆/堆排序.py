"""

@Author: Li Zenghui
@Date: 2020-03-28 22:38
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def siftup(lst, temp, begin, end):
            if lst == []:
                return []
            i, j = begin, begin * 2 + 1
            while j < end:
                if j + 1 < end and lst[j + 1] > lst[j]:
                    j += 1
                elif temp > lst[j]:
                    break
                else:
                    lst[i] = lst[j]
                    i, j = j, 2 * j + 1
            lst[i] = temp

        def heap_sort(lst):
            if lst == []:
                return []
            end = len(lst)
            for i in range((end // 2) - 1, -1, -1):
                siftup(lst, lst[i], i, end)
            for i in range(end - 1, 0, -1):
                temp = lst[i]
                lst[i] = lst[0]
                siftup(lst, temp, 0, i)
            return lst

        if tinput == [] or k > len(tinput):
            return []
        tinput = heap_sort(tinput)
        return tinput[: k]