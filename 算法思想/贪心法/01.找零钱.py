"""
存在面额值为：{200， 100， 20， 10， 5， 1}
支付金额 x ，求最少张数
@Author: Li Zenghui
@Date: 2020-03-31 16:01
"""


def min_count(x):
    rmb = [200, 100, 20, 10, 5, 1]
    count = 0
    for i in range(len(rmb)):
        use = x//rmb[i]
        count += use
        x = x - use * rmb[i]

    return count


if __name__ == '__main__':
    print(min_count(28))

