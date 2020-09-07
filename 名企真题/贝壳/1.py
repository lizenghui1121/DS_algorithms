"""

@Author: Li Zenghui
@Date: 2020-09-07 15:06
"""


def compare(s1, s2):
    if s1 == "S" and s2 == "J":
        return 1
    if s1 == "J" and s2 == "B":
        return 1
    if s1 == "B" and s2 == "S":
        return 1
    return 0


t = int(input())

for _ in range(t):
    l1, r1, l2, r2 = input().split()
    left_rate = 0
    right_rate = 0
    left_rate = compare(l1, l2) + compare(l1, r2)
    right_rate = compare(r1, l2) + compare(r1, r2)
    if left_rate > right_rate:
        print("left")
    elif left_rate < right_rate:
        print("right")
    else:
        print("same")
