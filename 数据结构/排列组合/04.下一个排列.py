"""
返回下一个排列， 比现在大的
@Author: Li Zenghui
@Date: 2020-06-29 15:49
"""


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            nums[i:] = sorted(nums[i:])
            for j in range(i, len(nums)):
                if nums[j] > nums[i - 1]:
                    nums[j], nums[i - 1] = nums[i - 1], nums[j]
                    break
            return
    nums.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    nextPermutation(nums1)
    print(nums1)
    nextPermutation(nums2)
    print(nums2)
