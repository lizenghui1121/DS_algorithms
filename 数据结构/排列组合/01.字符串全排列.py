"""

@Author: Li Zenghui
@Date: 2020-03-25 19:50
"""

import itertools


def permutation(s):
    if not s:
        return []
    res = []
    k = itertools.permutations(s)
    for item in k:
        print(item)
        res.append("".join(item))
    res = list(set(res))
    res.sort()
    return res


if __name__ == '__main__':
    print(permutation('abcb'))
