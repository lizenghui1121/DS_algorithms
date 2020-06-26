import numpy as np


def softMax(x):

    xmax = np.max(x)
    fenzi = np.exp(x - xmax)
    fenmu = np.sum(np.exp(x - xmax))

    return fenzi / fenmu

def function(data, w1, w2):
    # A = w1 @ data
    # print(w1)
    # print(w1.shape)
    # print(data.T)
    data = data.reshape(data.shape[0], 1)
    print(data)
    A = np.dot(w1, data)
    A = np.maximum(0, A)
    # Z = w2 @ A
    # Z = w2.dot(A)
    Z = np.dot(w2, A)
    print(Z)
    Y = softMax(Z)
    print(Y)
    output01 = np.max(Y)
    index_01 = np.argmax(Y)

    return output01, index_01


if __name__ == "__main__":
    N, M = map(int, input().split())
    data = np.array(list(map(int, input().split())))

    element = list(map(float, input().split()))
    w1 = []
    for i in range(M):
        w_x = []
        for j in range(N):
            w_x.append(element[i*N+j])
        w1.append(w_x)
    w1 = np.array(w1)

    element2 = list(map(float, input().split()))
    w2 = []
    for i in range(10):
        w_x = []
        for j in range(M):
            w_x.append(element2[i*M + j])
        w2.append(w_x)
    w2 = np.array(w2)

    max_, max_index = function(data, w1, w2)
    print(max_, max_index)


    change01 = 0
    change01_num = []
    change01_index = []

    change02_num = []
    change02_index = []
    for i in range(len(data)):
        for num in range(-128, 128):
            data_list = data.copy()
            print(data_list)
            data_list[i] = num
            max_num, max_index_num = function(data_list, w1, w2)
            print(max_num, max_index_num)
            if max_index_num != max_index:
                change01 = 1
                change01_num.append(max_num)
                change01_index.append([max_index_num, num])
    if change01 == 1:
        index = max(change01_num)
        P, Q = change01_index[change01_num.index(index)]
        print(P, Q)


