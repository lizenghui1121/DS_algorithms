"""

@Author: Li Zenghui
@Date: 2020-08-31 21:01
"""


def maximumSwap(num):
    """
    :type num: int
    :rtype: int
    """
    s = list(str(num))
    last = [0] * 10
    for i in range(len(s)):
        last[int(s[i])] = i
    for i in range(len(s)):
        for j in range(9, int(s[i]), -1):
            if last[j] > i:
                s[i], s[last[j]] = s[last[j]], s[i]
                print(s)
                break

    return int("".join(s))


if __name__ == '__main__':
    print(maximumSwap(2736))