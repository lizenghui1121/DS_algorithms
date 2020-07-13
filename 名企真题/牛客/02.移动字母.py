"""

@Author: Li Zenghui
@Date: 2020-07-09 22:08
"""


def change(s):
    # write code here
    s_list = list(s)
    slow = 0
    for i in range(len(s_list)):
        if s_list[i] != 'a':
            s_list[slow] = s_list[i]
            slow += 1
    for i in range(slow, len(s_list)):
        s_list[i] = 'a'
    return ''.join(s_list)


if __name__ == '__main__':
    print(change('abacde'))