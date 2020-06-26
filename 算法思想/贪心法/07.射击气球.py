"""
描述：
平面上有一定气球，平面可看作坐标系，在x轴上安排弓箭手向y轴方向射箭，求最少需要多少弓箭手
示例：
输入：[[10, 16],[2, 8],[1, 6],[7, 12]]
输出：2
@Author: Li Zenghui
@Date: 2020-03-31 20:12
"""


def find_min_arrow_shot(arr):
    arr.sort(key=lambda x: x[0])
    print(arr)
    shoot_num = 1
    short_begin = arr[0][0]
    short_end = arr[0][1]
    for i in range(len(arr)):
        if short_end >= arr[i][0]:
            short_begin = arr[i][0]
            if short_end > arr[i][1]:
                short_end = arr[i][1]
        else:
            shoot_num += 1
            short_begin = arr[i][0]
            short_end = arr[i][1]
    return shoot_num


if __name__ == '__main__':
    print(find_min_arrow_shot([[1, 2], [3, 4], [4, 6], [7, 8]]))
