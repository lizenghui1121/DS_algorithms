"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

@Author: Li Zenghui
@Date: 2020-07-14 15:29
"""
import collections
import heapq
def topKFrequent(nums, k):
    dic = {x: 0 for x in nums}
    for i in range(len(nums)):
        dic[nums[i]] += 1
    print(dic.items())
    entrys = dic.items()
    entrys = sorted(entrys, key=lambda b: b[1], reverse=True)
    res = []
    for i in range(k):
        res.append(entrys[i][0])
    return res


def topKFrequent2(nums, k):
   count = collections.Counter(nums)
   return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3]
    print(topKFrequent(arr, 2))
    print(topKFrequent2(arr, 2))
