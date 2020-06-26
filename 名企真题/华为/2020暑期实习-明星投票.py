"""

@Author: Li Zenghui
@Date: 2020-04-15 17:19
"""
name_list = input().split(",")
d = {i: 0 for i in name_list}

def f(name_list, d):
    for item in name_list:
        flag = True
        if 'A' <= item[0] <= 'Z':
            for char in item[1:]:
                if char < 'a' or char > 'z':
                    flag = False
                    return 'error.0001'
        else:
            flag = False
            return 'error.0001'

        if flag:
            d[item] += 1
    max_vote_num = 0
    res = []
    for name in d:
        if d[name] > max_vote_num:
            max_vote_num = d[name]
            res = [name]
        if d[name] == max_vote_num:
            res.append(name)
    res.sort()
    return res[0]

print(f(name_list, d))
