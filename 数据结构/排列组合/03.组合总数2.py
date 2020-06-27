"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次

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
    s = set()

    def dfs(path, i, n, res):
        if sum(path) == target:
            path_str = ''.join(map(str, path))
            if path_str not in s:
                res.append(path.copy())
                s.add(path_str)
            return
        if i > n-1:
            return
        if sum(path) < target:
            path.append(candidates[i])
            print(path)
            dfs(path, i + 1, n, res)
            path.pop()
            dfs(path, i + 1, n, res)

    dfs(path, 0, n, res)
    return res


if __name__ == '__main__':
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(combination_sum(candidates, target))
