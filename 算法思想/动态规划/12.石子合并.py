"""
设有N堆石子排成一排，其编号为1，2，3，…，N。
每堆石子有一定的质量，可以用一个整数来描述，现在要将这N堆石子合并成为一堆。
每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和，合并后与这两堆石子相邻的石子将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同。
例如有4堆石子分别为 1 3 5 2， 我们可以先合并1、2堆，代价为4，得到4 5 2， 又合并 1，2堆，代价为9，得到9 2 ，再合并得到11，总代价为4+9+11=24；
如果第二步是先合并2，3堆，则代价为7，得到4 7，最后一次合并代价为11，总代价为4+7+11=22。
问题是：找出一种合理的方法，使总的代价最小，输出最小代价。
输入格式
第一行一个数N表示石子的堆数N。
第二行N个数，表示每堆石子的质量(均不超过1000)。
输出格式
输出一个整数，表示最小代价。
@Author: Li Zenghui
@Date: 2020-08-04 14:51
"""


def min_cost(n, arr):
    s = [0]
    for num in arr:
        s.append(s[-1] + num)
    print(s)
    f = [[0] * (n + 1) for _ in range(n + 1)]
    for m_len in range(2, n+1):
        for i in range(1, n-m_len+2):
            j = i + m_len - 1
            f[i][j] = float('inf')
            for k in range(i, j):
                f[i][j] = min(f[i][j], f[i][k] + f[k+1][j] + s[j] - s[i-1])
    return f[1][n]


if __name__ == '__main__':
    # n = int(input())
    # w = list(map(int, input().split()))
    # s = [0]  # 前缀和
    # for num in w:
    #     s.append(s[-1] + num)
    # print(s)
    # dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    # for m_len in range(2, n + 1):
    #     for i in range(1, n - m_len + 2):
    #         j = i + m_len - 1
    #         for k in range(i, j):
    #             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[j] - s[i - 1])
    #
    # print(dp[1][n])
    print(min_cost(4, [1, 3, 5, 2]))
