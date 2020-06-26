"""
复制一个链表，要求是深拷贝，原链表存在random指针
@Author: Li Zenghui
@Date: 2020-03-11 21:26
"""

from list_node import ListNode
# -*- coding:utf-8 -*-


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def copy_random_list(self, head):
        node_map = {}
        node_vec = []
        ptr = head
        i = 0
        while ptr:
            node_vec.append(RandomListNode(ptr.label))
            node_map[ptr] = i
            i += 1
            ptr = ptr.next
        node_vec.append(0)
        ptr = head
        i = 0
        while ptr:
            node_vec[i].next = node_vec[i+1]
            if ptr.random:
                random_id = node_map[ptr.random]
                node_vec[i].random = node_vec[random_id]
            ptr = ptr.next
            i += 1
        return node_vec[0]


if __name__ == '__main__':
    a1 = RandomListNode(1)
    a2 = RandomListNode(2)
    a3 = RandomListNode(3)
    a4 = RandomListNode(4)
    a5 = RandomListNode(5)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    a1.random = a3
    a2.random = a4
    a5.random = a5

    s = Solution()
    new_head = s.copy_random_list(a1)
    while new_head:
        print(new_head.label)
        if new_head.random:
            print("random为", new_head.random.label)
        new_head = new_head.next
