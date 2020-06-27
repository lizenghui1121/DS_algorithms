"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
@Author: Li Zenghui
@Date: 2020-06-27 16:52
"""


def combination_sum(candidates, target):
    n = len(candidates)
    if n == 0:
        return []
    candidates.sort()
    path = []
    res = []

    def dfs(path, begin, n, res):
        if sum(path) == target:
            res.append(path.copy())
            return
        for i in range(begin, n):
            if sum(path) < target:
                path.append(candidates[i])
                dfs(path, i, n, res)
                path.pop()

    dfs(path, 0, n, res)
    return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum(candidates, target))
