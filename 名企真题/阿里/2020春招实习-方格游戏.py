"""

@Author: Li Zenghui
@Date: 2020-04-08 20:44
"""
import collections


def get_max(nums, n, k):

    def dfs(nums, x, y, n, count):
        mark[x][y] = 1
        count.append(nums[x][y])
        print(count)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        flag = 0
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx < 0 or newx >= n or newy< 0 or newy >=n or nums[x][y] >= nums[newx][newy]:
                flag += 1
                if flag == 4:
                    res.append(sum(count))
                    print(max(res))
                continue
            else:
                dfs(nums, newx, newy, n, count)
                count.pop()

    mark = [[0 for j in range(n)] for i in range(n)]
    count = []
    res = []  # 记录每次步数走完，count值
    dfs(nums, 0, 0, n, count)
    return max(res)


def gridgame1(array,n,k):
    if n == 0 : return 0
    queue = collections.deque()
    queue.append((0,0,array[0][0]))
    max_fees = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        tmp = queue.popleft()
        x,y,fee = tmp
        max_fees = fee if fee > max_fees else max_fees
        print(queue)
        for i in range(4):
            for step in range(1,k+1):
                nx = x + step*dx[i]
                ny = y + step*dy[i]
                if nx >= 0 and nx <=n-1 and ny >= 0 and ny <= n-1 and array[nx][ny] > array[x][y]:
                    queue.append((nx,ny,array[nx][ny] + fee))
    print(max_fees)


def find_max_path_v1(arr, n, K_):
    dp = []
    for i in range(n):
        dp.append([-1] * n)
    dp[0][0] = arr[0][0]
    max_sum = -1
    for i in range(0, n):
        for j in range(0, n):
            # 不能走斜线
            for k in range(max(i-K_, 0), min(i+K_+1, n)):
                l=j
                if arr[k][l] > arr[i][j] and dp[i][j] > -1:
                    dp[k][l] = max(dp[k][l], dp[i][j] + arr[k][l])
                    if dp[k][l] > max_sum:
                        max_sum = dp[k][l]
            for l in range(max(j-K_, 0), min(j+K_+1, n)):
                k=i
                if arr[k][l] > arr[i][j] and dp[i][j] > -1:
                    dp[k][l] = max(dp[k][l], dp[i][j] + arr[k][l])
                    if dp[k][l] > max_sum:
                        max_sum = dp[k][l]
    print(dp)
    return max_sum


# t = int(input())
# n, k = map(int, input().split(' '))
#
# for i in range(t):
#     nums = [[j for j in map(int, input().split(' '))] for i in range(n)]
#     print(get_max(nums, n, k))
test_arr = [[1, 2, 5],
            [10, 11, 6],
            [12, 12, 7]]
t = 1
n = 3
k = 1
print(get_max(test_arr, n, k))
# print(find_max_path_v1(test_arr, n, k))
gridgame1(test_arr, n, k)

