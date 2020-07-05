"""

@Author: Li Zenghui
@Date: 2020-07-05 10:47
"""


def get_last_moment(n, left, right):
    if not left:
        max_left = 0
    else:
        max_left = max(left)
    if not right:
        max_right = 0
    else:
        max_right = n - min(right)
    return max(max_left, max_right)


if __name__ == '__main__':
    n = 7
    left = [0,1,2,3,4,5,6,7]
    right = []
    print(get_last_moment(n, left, right))