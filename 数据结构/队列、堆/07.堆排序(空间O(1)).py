"""

@Author: Li Zenghui
@Date: 2020-03-29 20:00
"""


# 下沉操作
def down_ajust(arr, parent, length):
    """下沉操作,执行删除后,相当于把最后一个元素赋给根元素后,执行下沉操作
    :param arr
    :param parent 要下沉元素的下标
    :param length 数组的长度
    """
    temp = arr[parent]  # 临时保存要下沉的元素
    child = 2 * parent + 1
    while child < length:
        # 如果右孩子比左孩子小,则定位到右孩子
        if child+1 < length and arr[child+1] < arr[child]:
            child += 1
        # 如果父节点比孩子节点小或等于,则下沉结束
        if temp <= arr[child]:
            break
        # 单向赋值
        arr[parent] = arr[child]
        parent = child
        child = 2 * parent + 1
    arr[parent] = temp
    return arr


def heap_sort(arr, length):
    # 构建二叉堆
    for i in range(length//2-1, -1, -1):
        down_ajust(arr, i, length)

    # 运行堆排序
    for i in range(length-1, -1, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        down_ajust(arr, 0, i)
    return arr


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 0, 10, 6]
    print(heap_sort(arr, len(arr)))
