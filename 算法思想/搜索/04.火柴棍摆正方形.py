"""
已知一个数组，保存了n(n<15)个火柴棍，问可否用这n个火柴棍摆成一个正方形。
@Author: Li Zenghui
@Date: 2020-04-01 18:17
"""


def make_square(nums):
    if len(nums) < 4:
        return False
    length_sum = sum(nums)
    if length_sum % 4 != 0:
        return False
    nums.sort(reverse=True)
    bucket = [0 for i in range(4)]
    return generate(0, nums, length_sum / 4, bucket)


def generate(i, nums, target, bucket):
    if i >= len(nums):
        return bucket[0] == target and bucket[1] == target and bucket[2] == target and bucket[3] == target
    for j in range(4):
        if bucket[j] + nums[i] > target:
            continue
        bucket[j] += nums[i]
        if generate(i + 1, nums, target, bucket):
            return True
        bucket[j] -= nums[i]
    return False


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2]
    print(make_square(nums))
