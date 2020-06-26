"""

@Author: Li Zenghui
@Date: 2020-03-24 20:58
"""


def longest_palindrome(s):
    hash_map = [0 for i in range(128)]
    max_length = 0
    flag = 0
    for i in s:
        hash_map[ord(i)] += 1

    for i in hash_map:
        if i % 2 == 0:
            max_length += i
        else:
            max_length += i-1
            flag = 1
    return max_length + flag


if __name__ == '__main__':
    print(longest_palindrome('abcba'))
    print(longest_palindrome('aaabbbccc'))