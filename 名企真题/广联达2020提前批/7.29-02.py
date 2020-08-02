"""
题目描述：
我们希望一个序列中的元素是各不相同的，但是理想和现实往往是有差距的。现在给出一个序列A，其中难免有些相同的元素，现在提供了一种变化方式，使得经过若干次操作后一定可以得到一个元素各不相同的序列。
这个操作是这样的，令x为序列中最小的有重复的数字，你需要删除序列左数第一个x，并把第二个x替换为2*x。
请你输出最终的序列。
例如原序列是[2,2,1,1,1],一次变换后变为[2,2,2,1]，两次变换后变为[4,2,1]，变换结束

输入描述
输入第一行包含一个正整数n，表示序列的长度为n。(1<=n<=50000)  第二行有n个整数，初始序列中的元素。(1<=a_i<=10^8)  输出描述
输出包含若干个整数，即最终变换之后的结果。
@Author: Li Zenghui
@Date: 2020-07-29 22:47
"""
import heapq

n = int(input())
nums = [int(_) for _ in input().split()]


# n = 5
# nums = [5,1,4,5,4]

def init(nums):
    statistic = {}
    for i, x in enumerate(nums):
        if x not in statistic:
            statistic[x] = [i]
        else:
            heapq.heappush(statistic[x], i)
    return statistic


def main(nums):
    stat = init(nums)
    keys = list(stat.keys())
    heapq.heapify(keys)
    while keys:
        k = heapq.heappop(keys)  # 每次选择序列中的最小值
        while k in stat and len(stat[k]) >= 2:  # 若该值出现次数大于等于2
            idx1 = heapq.heappop(stat[k])
            idx2 = heapq.heappop(stat[k])
            x = nums[idx1] * 2

            nums[idx1] = 0
            nums[idx2] = x

            if x in stat:
                heapq.heappush(stat[x], idx2)
            else:
                stat[x] = [idx2]
                heapq.heappush(keys, x)
    nums = [i for i in nums if i > 0]
    return nums


res = main(nums)
for i in res:
    print(i, end=' ')
print()