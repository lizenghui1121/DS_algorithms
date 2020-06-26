"""
pattern = "abba" str = "dog cat cat dog" 匹配
@Author: Li Zenghui
@Date: 2020-03-25 14:53
"""


# 设置字符串到pattern的映射，用used[128]记录pattern字符是否已经用过
def word_pattern(pattern, raw_s):

    word_map = {}
    used = [0 for i in range(128)]
    pattern_len = len(pattern)
    s_list = raw_s.split(" ")
    if len(s_list) != pattern_len:
        return False
    pos = 0
    for word in s_list:
        if word not in word_map.keys():
            if used[ord(pattern[pos])] == 1:
                return False
            word_map[word] = pattern[pos]
            used[ord(pattern[pos])] = 1
        elif word_map[word] != pattern[pos]:
            return False
        pos += 1
    return True


if __name__ == '__main__':
    print(word_pattern("abba", "cat dog dog cat"))
    print(word_pattern("abb", "cat dog dog cat"))
    print(word_pattern("abba", "cat dog dog"))
    print(word_pattern("abba", "cat dog dog fish"))
    print(word_pattern("abbc", "cat dog dog fish"))
    print(word_pattern("abbc", "cat dog dog dog"))
