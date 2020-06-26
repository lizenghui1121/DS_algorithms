"""
描述：
已知一个数组（无重复元素），求这个数组构成的所有子集，子集里面没有重复的子集
@Author: Li Zenghui
@Date: 2020-04-06 13:55
"""


def find_subsets(nums):
    def generate(i, nums, item, result):
        if i >= len(nums):
            return
        item.append(nums[i])
        result.append(item[:])
        generate(i + 1, nums, item, result)
        item.pop()
        generate(i + 1, nums, item, result)

    item = []
    result = []
    result.append(item)
    generate(0, nums, item, result)
    return result


def find_subsets_bit(nums):
    all_set = 1 << len(nums)
    res = []
    for i in range(all_set):
        item = []
        for j in range(len(nums)):
            print(i & (1 << j))
            if i & (1 << j):
                item.append(nums[j])
        res.append(item)
    return res


if __name__ == '__main__':
    print(find_subsets([1, 2, 3, 4]))
    print(find_subsets_bit([1, 2, 3]))
