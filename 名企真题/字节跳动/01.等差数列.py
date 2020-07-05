"""

@Author: Li Zenghui
@Date: 2020-07-05 10:32
"""


def f(nums):
    if len(nums) <= 2:
        return True
    list1 = sorted(nums)
    n = len(list1)
    gap = list1[1] - list1[0]
    for i in range(2, n):
        if list1[i] - list1[i-1] == gap:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    test_arr = [1, 1, 1]
    print(f(test_arr))
