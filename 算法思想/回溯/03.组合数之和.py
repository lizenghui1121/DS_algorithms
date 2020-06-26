"""
已知一个数组（有重复元素），求这个数组构成的所有子集，子集和为target的子集
@Author: Li Zenghui
@Date: 2020-04-06 14:50
"""


def combination_sum(nums, target):
    def generate(i, nums):
        if i >= len(nums) or sum(item) == target:
            return
        item.append(nums[i])
        if ''.join(list(map(str, item))) not in res_set and sum(item) == target:
            result.append(item.copy())
            res_set.add(''.join(list(map(str, item))))
        generate(i + 1, nums)
        item.pop()
        generate(i + 1, nums)

    res_set = set()
    item = []
    result = []
    nums.sort()
    generate(0, nums)
    return result


if __name__ == '__main__':
    print(combination_sum([10, 1, 2, 7, 6, 5], 8))
