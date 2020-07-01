"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
@Author: Li Zenghui
@Date: 2020-07-01 14:12
"""


def subsets(nums):
    def generate(i, nums, path, res):
        if i == len(nums):
            return
        path.append(nums[i])
        res.append(path.copy())
        generate(i + 1, nums, path, res)
        path.pop()
        generate(i + 1, nums, path, res)

    path = []
    res = [[]]
    generate(0, nums, path, res)
    return res


def subsets_2(nums):
    n = len(nums)
    output = []

    for i in range(2 ** n, 2 ** (n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return output


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
    print(subsets_2([1, 2, 3]))
