"""
求两个链表的交叉点
@Author: Li Zenghui
@Date: 2020-03-11 20:32
"""
from list_node import ListNode


class Solution1:

    def get_insection_node(self, head_a, head_b):
        s = set()
        while head_a:
            if head_a not in s:
                s.add(head_a)
            head_a = head_a.next

        while head_b:
            if head_b in s:
                return head_b
            head_b = head_b.next

        return None


class Solution2:

    def get_list_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def forward_list_long(self, long_len, short_len, head):
        delta = long_len - short_len
        while head and delta > 0:
            head = head.next
            delta -= 1
        return head

    def get_insection_node_2(self, head_a, head_b):
        len_a = self.get_list_length(head_a)
        len_b = self.get_list_length(head_b)
        if len_a > len_b:
            head_a = self.forward_list_long(len_a, len_b, head_a)
        else:
            head_b = self.forward_list_long(len_b, len_a, head_b)

        while head_a and head_b:
            if head_a == head_b:
                return head_a
            head_a = head_a.next
            head_b = head_b.next
        return None


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    head_1 = n1
    m1 = ListNode(7)
    m2 = ListNode(8)
    m3 = ListNode(9)
    m1.next = m2
    m2.next = m3
    m3.next = n3
    head_2 = m1

    # s = Solution1()
    # res = s.get_insection_node(head_1, head_2)
    # print(res.val)
    s = Solution2()
    res = s.get_insection_node_2(head_1, head_2)
    print(res.val)

