"""

@Author: Li Zenghui
@Date: 2020-08-29 15:28
"""

def get_next(t):
    i = 0
    j = -1
    next_value = [-1] * len(t)
    while i < len(t) - 1:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            if i < len(t) and t[i] != t[j]:
                next_value[i] = j
            else:
                next_value[i] = next_value[j]
        else:
            j = next_value[j]
    return next_value

def kmp(s, t):
    i = 0
    j = 0
    next_val = get_next(t)
    while i < len(s) and j < len(t):
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next_val[j]
    if j == len(t):
        return i - j
    else:
        return -1

if __name__ == '__main__':
    haystack = 'acabaabaabcacaabc'
    needle = 'abaabcac'

    print(kmp(haystack, needle))    # 输出 "5"