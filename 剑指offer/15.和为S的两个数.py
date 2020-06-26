"""

@Author: Li Zenghui
@Date: 2020-04-04 22:12
"""

def FindNumbersWithSum(array, tsum):
    import itertools
    min_mul = float('inf')
    all_permutation = itertools.permutations(array, 2)
    for item in all_permutation:
        if sum(item) == tsum:
            mul = item[0] * item[1]
            if mul < min_mul:
                min_mul = mul
                res=list(item)
    return res


if __name__ == '__main__':
    print(FindNumbersWithSum([1, 2, 3, 5, 6, 7], 7))
    res = []
    print(res.append([1, 2]))
    print(res)