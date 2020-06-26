"""
给一个DNA字符串，找出所有长度超过10，切出现次数超过1次的子串。
@Author: Li Zenghui
@Date: 2020-03-25 16:32
"""


# 方法1，长度为10, 按顺序遍历，固定长度为10，将字符串存入哈希表。最后统计次数大于1的key值
def find_repeat_substring(s):
    end = len(s)-10
    word_map = {}
    for i in range(end+1):
        key = s[i:i+10]
        if key not in word_map.keys():
            word_map[key] = 1
        else:
            word_map[key] += 1
    res = []
    for key, value in word_map.items():
        if value > 1:
            res.append(key)
    return res


if __name__ == '__main__':
    print(find_repeat_substring('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
    print(find_repeat_substring('AAAAAAAAAAA'))
    print(find_repeat_substring('AAAAAAAA'))
