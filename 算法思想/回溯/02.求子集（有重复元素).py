"""
描述：
已知一个数组（有重复元素），求这个数组构成的所有子集，子集里面没有重复的子集
@Author: Li Zenghui
@Date: 2020-04-06 14:37
"""


def find_subsets(nums):
    def generate(i, nums, item, result, res_set):
        if i >= len(nums):
            return
        item.append(nums[i])
        if ''.join(list(map(str, item))) not in res_set:
            result.append(item[:])
            res_set.add(''.join(list(map(str, item))))
        generate(i + 1, nums, item, result, res_set)
        item.pop()
        generate(i + 1, nums, item, result, res_set)
    res_set = set()
    item = []
    result = []
    nums.sort()
    result.append(item)
    generate(0, nums, item, result, res_set)
    return result


def find_subsets_bit(nums):
    all_set = 1 << len(nums)
    nums.sort()
    res = []
    for i in range(all_set):
        item = []
        for j in range(len(nums)):
            if i & (1 << j):
                item.append(nums[j])
        res.append(item)
    return res


if __name__ == '__main__':
    print(find_subsets([1, 2, 2, 2]))
    # print(find_subsets_bit([1, 2, 2, 2]))
