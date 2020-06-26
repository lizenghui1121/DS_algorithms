"""
求两个链表，如果存在环，返回环节点
@Author: Li Zenghui
@Date: 2020-03-11 20:57
"""

from list_node import ListNode

# set集合法
class Solution1:

    def detect_cycle(self, head):
        s = set()
        while head:
            if head not in s:
                s.add(head)
            else:
                return head
            head = head.next
        return None


class Solution2:

    def detect_cycle_2(self, head):
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:
                meet = fast
                break

        if not meet:
            return None
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next
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
    n5.next = n2
    head = n1
    # s = Solution1()
    # res = s.detect_cycle(head)
    # print(res.val)
    s = Solution2()
    res = s.detect_cycle_2(head)
    print(res.val)

