"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。

@Author: Li Zenghui
@Date: 2020-07-03 14:26
"""


def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    # dp[i] 表示字符串 s 前 i 个字符组成的字符串
    # s[0..i-1]是否能被空格拆分成若干个字典中出现的单词
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(0, i):
            print(s[j:i])
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
    return dp[n]


if __name__ == '__main__':
    s = "appleandapple"
    word_list = ["apple", "and"]
    print(word_break(s, word_list))
