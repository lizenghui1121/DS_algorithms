"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

@Author: Li Zenghui
@Date: 2020-07-16 12:12
"""


def findAnagrams(s, p):
    def is_window_ok(window_map, p_map):
        for c in window_map:
            if window_map[c] != p_map[c]:
                return False
        for c in p_map:
            if p_map[c] != window_map[c]:
                return False
        return True

    import collections
    p_len = len(p)
    s_len = len(s)
    if p_len > s_len:
        return 0
    window_map = collections.defaultdict(int)
    p_map = collections.defaultdict(int)
    for c in p:
        p_map[c] += 1

    begin = 0
    res = []
    for i in range(s_len):
        window_map[s[i]] += 1
        while begin < i:
            begin_ch = s[begin]
            if begin_ch not in p_map:
                begin += 1
                window_map[begin_ch] -= 1
            elif window_map[begin_ch] > p_map[begin_ch]:
                window_map[begin_ch] -= 1
                begin += 1
            else:
                break
        if is_window_ok(window_map, p_map):
            res.append(begin)
    return res


if __name__ == '__main__':
    s = "abab"
    p = "ab"
    print(findAnagrams(s, p))
