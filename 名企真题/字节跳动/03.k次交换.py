"""

@Author: Li Zenghui
@Date: 2020-07-05 11:19
"""


def ismin(i, array, K):
    # print i
    # print array
    # print K
    if (K + 1) < len(array):
        if array[i] == min(array[0:K + 1]):
            return True
        else:
            return False
    else:
        if array[i] == min(array[0:]):
            return True
        else:
            return False


##从最大值向前面逐个交换
def new_trans_k(array, index_max, k):
    for i in range(k):
        t = array[index_max]
        array[index_max] = array[index_max - 1]
        array[index_max - 1] = t
        index_max -= 1
    return array


# 数组转换
def trans(array, K):
    for i in range(K):
        # print 'i=',i
        # print 'K=',K
        if (K + 1) < len(array):
            if ismin(i, array, K):
                continue
            else:
                min_num = min(array[i:i + K + 1])
                index_max = array.index(min_num)
                c = index_max - i
                K = K - c
                array = new_trans_k(array, index_max, c)
        else:
            if i < len(array):
                if ismin(i, array, K):
                    continue
                else:
                    min_num = min(array[i:])
                    index_max = array.index(min_num)
                    c = index_max - i
                    K = K - c
                    array = new_trans_k(array, index_max, c)
            else:
                break

    return array


if __name__ == '__main__':
    num = "9438957234785635408"
    array = list(map(int, num))
    k = 23
    array = trans(array, k)
    num_list_string = "".join(map(str, array))
    print(num_list_string)

