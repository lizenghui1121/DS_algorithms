"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
@Author: Li Zenghui
@Date: 2020-03-02 21:57
"""
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0;
        return pow(2, number-1)


