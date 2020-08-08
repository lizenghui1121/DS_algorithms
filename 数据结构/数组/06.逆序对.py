"""

@Author: Li Zenghui
@Date: 2020-08-08 12:13
"""


class Solution:
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, nums):
        def merge(nums, start, mid, end, temp):
            i = start
            j = mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            temp.clear()

        def merge_sort(nums, start, end, temp):
            if start >= end:
                return
            mid = start + (end - start) // 2
            merge_sort(nums, start, mid, temp)
            merge_sort(nums, mid+1, end, temp)
            merge(nums, start, mid, end,temp)
        merge_sort(nums, 0, len(nums) - 1, [])
        return self.cnt


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([7,5,6,4]))
