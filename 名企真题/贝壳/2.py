"""

@Author: Li Zenghui
@Date: 2020-09-07 15:15
"""

import collections


def min_steps(s):
    if not s:
        return 0
    q = collections.deque()
    q.append((s[0], 1, True))
    while q:
        cur, step, flag = q.popleft()
        if cur == s:
            return step
        if flag:
            q.append((cur + s[len(cur)], step + 1, flag))
            if cur == s[len(cur): len(cur) + len(cur)]:
                q.append((cur + cur, step + 1, False))
        else:
            q.append((cur + s[len(cur)], step + 1, flag))


n = int(input())
s = input()
print(min_steps(s))
