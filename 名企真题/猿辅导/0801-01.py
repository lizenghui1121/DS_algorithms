"""
小猿非常热爱学习，所以他在猿辅导上购买了NN节课来提升自己，每节课有一个开始时间SS和结束时间EE（SS和EE均用正整数表示）。
买完课程后，粗心的小袁发现这些课程之间有些时间冲突，幸好小猿有一种“一心多用”的超能力，能同时兼顾KK节课上课。
当然是KK越大，使用这种能力就越累。请问小猿最少需要一心几用，才能上完所有他买的课程呢？
输入描述
第一行输入为NN（N≤200000N≤200000），表示购买课程数。
接下来NN行，每行输入两个数Si、EiSi、Ei（0<Si<Ei<1e90<Si<Ei<1e9），为第ii节课的起止时间
输出描述
请输出最小满足条件的K
示例1
输入
4
1 4
1 2
2 3
3 4
输出
2

解题思路： (堆) O(nlog(n))
    1. 按开始时间和结束时间从小到大排序
    2. 使用堆维护时间区间，对于排序后两个课程aa和bb来说，如果aa和bb无法分开上，则须满足bb的开始时间小于aa的结束时间
    3. 答案为堆中同时存在的课程数量的最大值
@Author: Li Zenghui
@Date: 2020-08-07 21:05
"""
import heapq

n = int(input())
start_end_list = [list(map(int, input().split())) for _ in range(n)]
start_end_list.sort(key=lambda x: x[0])

q = []
res = 0
heapq.heapify(q)
for start, end in start_end_list:
    while q and q[0] <= start:
        heapq.heappop(q)
    heapq.heappush(q, end)
    res = max(res, len(q))
print(res)