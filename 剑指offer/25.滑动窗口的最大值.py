"""

@Author: Li Zenghui
@Date: 2020-04-05 22:24
"""


def maxInWindows(num, size):
    # write code here
    left = 0
    right = size - 1
    length = len(num)
    res = num[0]
    while right < length:
        temp_max = max(num[left:right + 1])
        if res < temp_max:
            res = temp_max
        left += 1
        right += 1
    return res

if __name__ == '__main__':
    print(maxInWindows([2, 4, 5, 6, 7, 8]))