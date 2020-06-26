"""
反转链表
@Author: Li Zenghui
@Date: 2020-03-11 15:15
"""
from list_node import ListNode


class Solution:
    # 1.头插法
    def reverse_list(self, head):
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head

    # 从链表位置m到n，逆置
    def reverse_between(self, m, n, head):
        change_len = n-m+1
        res = head
        pre_head = None
        while head and m-1 > 0:
            pre_head = head
            head = head.next
            m = m - 1
        modify_list_tail = head
        new_head = None
        while head and change_len > 0:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
            change_len -= 1
        modify_list_tail.next = head

        if pre_head:
            pre_head.next = new_head
        else:
            res = new_head
        return res


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
    head = n1
    s = Solution()
    # new = s.reverse_list(head)
    # while new:
    #     print(new.val)
    #     new = new.next
    new_2 = s.reverse_between(1, 5, head)
    while new_2:
        print(new_2.val)
        new_2 = new_2.next
