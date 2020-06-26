"""

@Author: Li Zenghui
@Date: 2020-04-25 17:16
"""


def letterCombinations(digits):
    if not digits:
        return []
    nums = list(digits)
    print(nums)
    d = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    length = len(nums)
    res = []
    path = []

    def dfs(nums, depth, path, length):
        if depth == length:
            res.append("".join(path))
            return
        for char in d[nums[depth]]:
            path.append(char)
            dfs(nums, depth + 1, path, length)
            path.pop()

    dfs(nums, 0, path, length)
    return res


if __name__ == '__main__':
    print(letterCombinations('23'))
