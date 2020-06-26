"""
描述：
已知数组nums，求新数组count, count[i]代表了在num[i]右侧且比nums[i]小的元素的个数
@Author: Li Zenghui
@Date: 2020-04-06 16:32
"""


# O(n^2)解法
def count_smaller(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
        res.append(count)
    return res


# Nlog(N)解法,
def count_smaller_2(nums):
    def merge_two_arr(sub_1, sub_2, count):
        res = []
        i = 0
        j = 0
        while i < len(sub_1) and j < len(sub_2):
            if sub_1[i][0] < sub_2[j][0]:
                count[sub_1[i][1]] += j
                res.append(sub_1[i])
                i += 1
            else:
                res.append(sub_2[j])
                j += 1
        while i < len(sub_1):
            count[sub_1[i][1]] += j
            res.append(sub_1[i])
            i += 1
        while j < len(sub_2):
            res.append(sub_2[j])
            j += 1
        return res

    def merge_sort(arr, count):
        if len(arr) < 2:
            return arr
        mid = len(arr)//2
        sub_1 = arr[0:mid]
        sub_2 = arr[mid:]
        return merge_two_arr(merge_sort(sub_1, count),  merge_sort(sub_2, count), count)

    pair_arr = [[nums[i], i] for i in range(len(nums))]
    print(pair_arr)
    count = [0 for i in range(len(nums))]
    pair_arr = merge_sort(pair_arr, count)
    print(pair_arr)
    return count


if __name__ == '__main__':
    print(count_smaller([5, 2, 6, 1]))
    print(count_smaller_2([5, 2, 6, 1]))
    print(pow(2, 31))
