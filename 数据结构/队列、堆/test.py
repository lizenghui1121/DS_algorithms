"""

@Author: Li Zenghui
@Date: 2020-03-22 12:11
"""
import heapq
x = [6, 4, 5, 2, 1, 7, 3]
x.sort()
heapq.heapify(x)
heapq.heappush(x, 8)
print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.nsmallest(3, x))
heapq._heapify_max(x)
print(heapq._heappop_max(x))



