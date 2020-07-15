"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

@Author: Li Zenghui
@Date: 2020-07-14 16:40
"""


def decodeString(s):
    sta = []
    for c in s:
        if c == ']':
            sub = ''
            while sta[-1] != '[':
                sub = sta.pop() + sub
            sta.pop()
            num = ''
            while sta and sta[-1].isdigit():
                num = sta.pop() + num
            sta.append(int(num) * sub)
        else:
            sta.append(c)
    return ''.join(sta)


def decodeString2(s):
    import re
    def f(m):
        return int(m.group(1)) * m.group(2)

    while '[' in s:
        s = re.sub(r'(\d+)\[([A-Za-z]*)\]', f, s)
    return s


if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(decodeString(s))
    print(decodeString2(s))

