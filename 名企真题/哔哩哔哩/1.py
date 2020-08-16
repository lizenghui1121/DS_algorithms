
# num = int(input())
# num_8 = oct(num)
# print(str(num_8).count('7'))



def f(num):
    res = 0
    while num > 0:
        if num % 8 == 7:
            res += 1
        num = num // 8
    return res

print(f(15))