"""

@Author: Li Zenghui
@Date: 2020-08-08 16:46
"""


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


print(is_leap(2000))
print(is_leap(2100))
print(is_leap(2020))
