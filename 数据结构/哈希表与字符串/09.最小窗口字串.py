"""
已知字符串S和字符串T，求在S中最小窗口（区间）, 使得区间中包括了字符串T的所有字符
@Author: Li Zenghui
@Date: 2020-03-25 17:04
"""


def min_window(s, t):
    map_s = [0 for i in range(128)]
    map_t = [0 for i in range(128)]
    record = []  # 记录字符串t中有哪些字符

    for i in range(len(t)):
        map_t[ord(t[i])] += 1

    for i in range(len(map_t)):
        if map_t[i] > 0:
            record.append(i)
    print(record)
    result = ""   # 最小窗口对应的字符串
    window_begin = 0
    for i in range(len(s)):
        map_s[ord(s[i])] += 1
        while window_begin < i:
            begin_ch = s[window_begin]
            if map_t[ord(begin_ch)] == 0:
                window_begin += 1
            elif map_s[ord(begin_ch)] > map_t[ord(begin_ch)]:
                map_s[ord(begin_ch)] -= 1
                window_begin += 1
            else:
                break
        if is_window_ok(map_s, map_t, record):
            new_window_len = i - window_begin + 1
            if result == "" or len(result) > new_window_len:
                result = s[window_begin:i+1]
    return result


def is_window_ok(map_s, map_t, record):
    for i in range(len(record)):
        if map_s[record[i]] < map_t[record[i]]:
            return False
    return True


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'DOE'
    print(min_window(s, t))
