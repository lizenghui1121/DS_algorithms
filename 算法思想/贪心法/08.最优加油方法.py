"""

@Author: Li Zenghui
@Date: 2020-03-31 20:39
"""
import heapq


def get_minimum_stop(s, p, stop):
    """
    :param s:起点到终点的距离
    :param p: 起始油量
    :param stop: <加油站到终点的距离， 加油站汽油量>
    :return:最少加油次数
    """
    q = []
    result = 0
    stop.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(stop)):
        dis = s - stop[i][0]
        while q and p < dis:
            p += heapq.heappop(q)
            result += 1
        if not q and p < dis:
            return -1
        p = p - dis
        s = stop[i][0]
        heapq.heappush(q, stop[i][1])
    return result


if __name__ == '__main__':
    print(get_minimum_stop(25, 14, [[15, 2], [11, 5], [10, 3], [4, 4]]))
