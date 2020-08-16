"""

@Author: Li Zenghui
@Date: 2020-08-13 21:28
"""


class Solution:
    def solve(self, n, m, limit):
        import collections
        nums = [x + 1 for x in range(n)]
        dic = collections.defaultdict(set)
        for point in limit:
            dic[point.x].add(point.y)
            dic[point.y].add(point.x)
        res = self.find_subsets(nums, dic)
        return len(res)
    def find_subsets(self, nums, dic):
        def generate(i, nums, item, result):
            if i >= len(nums):
                return
            flag = False
            for a in item:
                if nums[i] in dic[a]:
                    flag = True
            if not flag:
                item.append(nums[i])
                result.append(item[:])
            generate(i + 1, nums, item, result)
            if not flag:
                item.pop()
                generate(i + 1, nums, item, result)

        item = []
        result = []
        result.append(item)
        generate(0, nums, item, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.solve(3, 2, [(1, 2), (2, 3)]))
