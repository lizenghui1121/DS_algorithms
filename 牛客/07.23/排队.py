"""

@Author: Li Zenghui
@Date: 2020-07-23 21:33
"""


class Solution:
    def getNumValidPairs(self, n, m, a):
        import heapq
        res = [0]
        def MergeSort(lists):
            nonlocal res
            if len(lists) <= 1:
                return lists
            num = int(len(lists) / 2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    res[0] += len(left) - l
            result += right[r:]
            result += left[l:]
            return result

        if n <= m:
            MergeSort(a)
        if n > m:
            tmp = a[:m]
            heapq.heapify(tmp)
            for i in range(m, n):
                value = heapq.heappop(tmp)
                a[i] += value
                heapq.heappush(tmp, a[i])
            MergeSort(a)
        return res[0]


if __name__ == '__main__':
    s = Solution()
    print(s.getNumValidPairs(5, 2, [1, 3, 2, 5, 4]))

