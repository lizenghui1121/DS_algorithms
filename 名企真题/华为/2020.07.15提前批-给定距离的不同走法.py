"""
给定距离，并给出各种步长， nums[0]....nums[n-1]，请问有多少种走法（不考虑走路顺序）,先走短的，再走长的，步长互异
示例：
输入
4
1 2
输出：
3
1 + 1 + 1 + 1 = 4
1 + 1 + 2 = 4
2 + 2 = 4
@Author: Li Zenghui
@Date: 2020-07-23 10:50
"""


def route_count(nums, distance):
    def dfs(path, begin, nums, path_value, target):
        nonlocal res
        if path_value == target:
            res += 1
        # 每次都从begin开始，保证下次遍历，不会遍历小步长
        for i in range(begin, len(nums)):
            # 路径总和小于目标值时才进入
            if path_value < target:
                path.append(nums[i])
                path_value += nums[i]
                dfs(path, i, nums, path_value, target)
                # 回溯
                path_value -= nums[i]
                path.pop()
    # 步长排序
    nums.sort()
    res = 0
    path = []  # 记录路径
    path_value = 0  # 当前行走的距离
    dfs(path, 0, nums, path_value, distance)
    return res


if __name__ == '__main__':
    nums = [1, 2]
    distance = 5
    print(route_count(nums, distance))  # 3 [1, 1, 1, 1, 1] [1, 1, 1, 2] [1, 2, 2]
