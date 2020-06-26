"""
给定字符串，移除k位
@Author: Li Zenghui
@Date: 2020-04-29 19:09
"""

s = input()
k = int(input())

def f(s, k):
    sta = [s[0]]
    for i in range(1, len(s)):
        num = s[i]
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
        res += sta.pop(0)
    return res

print(f(s, k))
