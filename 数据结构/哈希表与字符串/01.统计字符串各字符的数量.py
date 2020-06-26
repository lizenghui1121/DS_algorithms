"""

@Author: Li Zenghui
@Date: 2020-03-24 20:19
"""


def count_char(s):
    my_set = set()
    for i in s:
        my_set.add(i)
    for item in my_set:
        print(item+':', s.count(item))


def count_char_2(s):
    char_map = [0 for i in range(128)]
    for i in s:
        char_map[ord(i)] += 1
    for i in range(len(char_map)):
        if char_map[i] > 0:
            print(chr(i) + ":", char_map[i])


if __name__ == '__main__':
    count_char('abcabsdojfosdf')
    print("------")
    count_char_2('abcabsdojfosdf')
