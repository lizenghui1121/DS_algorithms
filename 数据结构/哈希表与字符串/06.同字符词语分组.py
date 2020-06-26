"""
出现的各个字符相同，则放到一起
例如：['ate', 'tea', 'abc', 'bca]
返回：[['ate', 'tea'], ['abc', 'bca]]
@Author: Li Zenghui
@Date: 2020-03-25 15:25
"""


def group_word_1(word_arr):
    anagram_map = {}
    for item in word_arr:
        key = "".join(sorted(item))
        if key not in anagram_map.keys():
            anagram_map[key] = [item]
        else:
            anagram_map[key].append(item)
    res = []
    for item in anagram_map.values():
        res.append(item)
    return res


if __name__ == '__main__':
    print(group_word_1(['ate', 'tea', 'aet', 'avc', 'cva', 'bat']))
