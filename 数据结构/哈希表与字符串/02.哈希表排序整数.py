"""

@Author: Li Zenghui
@Date: 2020-03-24 20:30
"""


def hash_sort(arr):
    hash_map = [0 for i in range(1000)]
    for i in range(len(arr)):
        hash_map[arr[i]] += 1

    for i in range(1000):
        for j in range(hash_map[i]):
            print(i)


if __name__ == '__main__':
    hash_sort([999, 1, 444, 7, 20, 9, 1, 3, 7, 7])