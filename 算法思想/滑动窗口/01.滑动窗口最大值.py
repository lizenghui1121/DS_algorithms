"""

@Author: Li Zenghui
@Date: 2020-07-13 15:37
"""
from collections import deque


# 双端队列
def maxSlidingWindow1(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    def clean_deque(index):
        if dq and dq[0] == index - k:
            dq.popleft()
        while dq and nums[index] > nums[dq[-1]]:
                dq.pop()

    dq = deque()
    max_id = 0
    for i in range(k):
        clean_deque(i)
        dq.append(i)
        if nums[i] > nums[max_id]:
            max_id = i
    res = [nums[max_id]]
    for j in range(k, n):
        clean_deque(j)
        dq.append(j)
        res.append(nums[dq[0]])
    return res


def max_slide_window(nums, k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n - 1]
    for i in range(1, n):
        # from left to right
        if i % k == 0:
            # block start
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])
        # from right to left
        j = n - i - 1
        if (j + 1) % k == 0:
            # block end
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])

    output = []
    for i in range(n - k + 1):
        output.append(max(left[i + k - 1], right[i]))

    return output


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow1(nums, k))
    print(max_slide_window(nums, k))
