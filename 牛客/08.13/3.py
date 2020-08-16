"""

@Author: Li Zenghui
@Date: 2020-08-13 21:43
"""

#
# 返回找到能够满足游戏胜利条件的子集，如果有多个子集满足条件，返回字典序最小的即可。
# @param n int整型 代表数字的数量
# @param k int整型 代表子集的大小
# @param s int整型一维数组 代表数字数组
# @return int整型一维数组
#
class Solution:
    def solve(self, n, k, s):


    def find_subsets(self, nums):
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
