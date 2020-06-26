"""

@Author: Li Zenghui
@Date: 2020-03-25 15:42
"""


def length_of_longest_substring(s):
    begin = 0
    res = 0
    word = ""
    char_map = [0 for i in range(128)]
    for i in range(len(s)):
        char_map[ord(s[i])] += 1
        if char_map[ord(s[i])] == 1:
            word += s[i]
            if res < len(word):
                res = len(word)
        else:
            while begin < i and char_map[ord(s[i])] > 1:
                char_map[ord(s[begin])] -= 1
                begin += 1
            word = s[begin:i+1]
    return res, word


if __name__ == '__main__':
    print(length_of_longest_substring('abcabdeab'))
