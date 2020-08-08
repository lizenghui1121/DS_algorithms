# n = int(input())
# a = list(map(int, input().split()))


def get_count(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return num // 2


# res = 0
# for num in a:
#     res += get_count(num)
def gcd(a, b):
    return gcd(b, a % b) if b else a


print(gcd(12, 6))
print(gcd(21, 12))
print(gcd(15, 35))
