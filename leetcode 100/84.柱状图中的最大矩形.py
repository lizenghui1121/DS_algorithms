"""

@Author: Li Zenghui
@Date: 2020-07-01 16:36
"""


# 暴力解法
def largest_rectangle_area(heights):
    n = len(heights)
    if n == 0:
        return 0
    res = 0
    for i in range(n):
        left = i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1

        right = i
        while right < n and heights[right] >= heights[i]:
            right += 1

        res = max(res, (right - left - 1) * heights[i])
    return res


# 单调栈, 两次遍历
def largest_rectangle_area_2(heights):
    n = len(heights)
    if n == 0:
        return 0
    left, right = [0] * n, [0] * n

    mono_stack = []
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)

    mono_stack = []
    for i in range(n - 1, -1, -1):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        right[i] = mono_stack[-1] if mono_stack else n
        mono_stack.append(i)
    area_list = [(right[i] - left[i] - 1) * heights[i] for i in range(n)]
    res = max(area_list)
    return res


# 单调栈，常数优化
def largest_rectangle_area_3(heights):
    n = len(heights)
    left, right = [0] * n, [n] * n

    mono_stack = list()
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            right[mono_stack[-1]] = i
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)

    ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
    return ans


if __name__ == '__main__':
    test_heigth = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(test_heigth))
    print(largest_rectangle_area_2(test_heigth))
    print(largest_rectangle_area_3(test_heigth))
