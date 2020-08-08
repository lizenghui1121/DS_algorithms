"""

@Author: Li Zenghui
@Date: 2020-08-08 16:39
"""


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(19))
print(is_prime(21))
