"""
给出一个区间的集合，请合并所有重叠的区间。
@Author: Li Zenghui
@Date: 2020-06-29 17:56
"""


def merge(intervals):
    n = len(intervals)
    if n == 0:
        return [[]]
    if n == 1:
        return intervals
    compare = lambda a: a[0]
    intervals = sorted(intervals, key=compare)
    res = [intervals[0]]
    for i in range(1, n):
        item1 = res[-1]
        item2 = intervals[i]
        if item1[1] >= item2[0]:
            res[-1][1] = max(item2[1], item1[1])
        else:
            res.append(item2)
    return res


if __name__ == '__main__':
    test_lists = [[1, 3], [2, 6], [8, 10], [15, 18]]
    test_lists2 = [[1, 4], [4, 5]]
    print(merge(test_lists))
    print(merge(test_lists2))
