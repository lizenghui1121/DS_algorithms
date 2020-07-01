"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

@Author: Li Zenghui
@Date: 2020-07-01 12:45
"""


def min_window(s, t):
    def check_valid(window_map, t_map):
        for c in t_map:
            if c not in window_map or window_map[c] < t_map[c]:
                return False
        return True

    word_window = {char: 0 for char in s}
    t_map = {c: 0 for c in t}
    for c in t:
        t_map[c] += 1
    res = ""
    begin = 0
    for i in range(len(s)):
        word_window[s[i]] += 1
        while begin < i:
            begin_ch = s[begin]
            if begin_ch not in t_map:
                begin += 1
            elif word_window[begin_ch] > t_map[begin_ch]:
                begin += 1
                word_window[begin_ch] -= 1
            else:
                break
        if check_valid(word_window, t_map):
            new_window_len = i - begin + 1
            if res == "" or len(res) > new_window_len:
                res = s[begin: i+1]
    return res


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(min_window(S, T))
