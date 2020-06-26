"""

@Author: Li Zenghui
@Date: 2020-06-05 10:03
"""
import numpy as np


def softMax(x):
    xmax = np.max(x)
    fenzi = np.exp(x - xmax)
    fenmu = np.sum(np.exp(x - xmax))

    return fenzi / fenmu


if __name__ == '__main__':
    z = np.array([1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0])
    print(np.exp(z) / sum(np.exp(z)))
    print(softMax(z))
