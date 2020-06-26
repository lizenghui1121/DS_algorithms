"""

@Author: Li Zenghui
@Date: 2020-04-04 22:59
"""


def IsContinuous(numbers):
    # write code here
    if not numbers:
        return False
    count_0 = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            count_0 += 1
    temp = count_0
    while temp > 0:
        numbers.remove(0)
        temp -= 1
    if len(list(set(numbers))) == len(numbers) and max(numbers) - min(numbers) <= 4:
        return True
    else:
        return False


if __name__ == '__main__':
    print(IsContinuous([1, 3, 2, 4, 5]))
