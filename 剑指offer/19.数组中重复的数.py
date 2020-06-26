"""

@Author: Li Zenghui
@Date: 2020-04-05 17:11
"""


def duplicate(numbers, duplication):
    # write code here
    if not numbers:
        return False
    arr = [0 for i in range(len(numbers))]
    for i in range(len(numbers)):
        if arr[numbers[i]] ==1:
            duplication[0] == numbers[i]
            return True
        else:
            arr[numbers[i]] += 1


if __name__ == '__main__':
    print(duplicate())