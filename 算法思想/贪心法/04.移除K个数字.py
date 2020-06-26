"""
描述：
已知一个使用字符串表示的非负整数num，将num中的k个数字移除，求移除k个数字后，可以获得的最小的可能的新数字。
示例：
输入：num = "1432219", k = 3
输出：1219
@Author: Li Zenghui
@Date: 2020-03-31 16:53
"""


# 方法1：暴力法
def remove_k_digit_1(s, k):
    for i in range(k):
        flag = 0
        for j in range(1, len(s)):
            if s[j - 1] > s[j]:
                s = s[0:j - 1] + s[j:]
                flag = 1
                break
        if flag == 0:
            s = s[:-1]
    return int(s)


def remove_k_digit_2(s, k):
    sta = [int(s[0])]
    i = 1
    for i in range(1, len(s)):
        num = int(s[i])
        while len(sta) > 0 and sta[-1] > num and k > 0:
            sta.pop()
            k -= 1
        if num != 0 or len(sta) != 0:
            sta.append(num)

    while len(sta) > 0 and k > 0:
        sta.pop()
        k -= 1

    res = ""
    while sta:
        res += str(sta.pop(0))
    return res


if __name__ == '__main__':
    print(remove_k_digit_1('10002', 1))
    print(remove_k_digit_2('1400032219', 4))
