"""
将小于x的放在前面，大于x的放后面，保持节点原来的相对位置
@Author: Li Zenghui
@Date: 2020-03-11 21:16
"""
from list_node import ListNode


class Solution:

    def partition(self, head, x):
        less_head = ListNode(-1)
        less_ptr = less_head
        more_head = ListNode(-1)
        more_ptr = more_head

        while head:
            if head.val < x:
                less_ptr.next = head
                less_ptr = head
            else:
                more_ptr.next = head
                more_ptr = head
            head = head.next
        less_ptr.next = more_head.next
        return less_head.next


if __name__ == '__main__':
    n1 = ListNode(5)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(1)
    n5 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    head = n1
    s = Solution()
    res = s.partition(head, 3)

    while res:
        print(res.val)
        res = res.next

