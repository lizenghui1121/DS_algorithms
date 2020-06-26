"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
@Author: Li Zenghui
@Date: 2020-03-02 20:10
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        p = listNode
        while p:
            res.insert(0, p.val)
            p = p.next
        return res