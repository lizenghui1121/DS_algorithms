"""
@Author: Li Zenghui
@Date: 2020-03-14 18:59
"""

def get_cycle_len(cur, cnt, st):
    if cur == st:
        return  cnt + 1
    else:
        return get_cycle_len(p[cur], cnt+1, st)

p = []
t = int(input())