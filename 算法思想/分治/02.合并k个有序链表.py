"""
合并K个有序链表，返回头节点
@Author: Li Zenghui
@Date: 2020-06-29 14:58
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge_k_list(self, lists):
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = self.merge_2_list(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge_2_list(self, l1, l2):
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(5)
    n4 = ListNode(7)
    n5 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    p1 = ListNode(11)
    p2 = ListNode(13)
    p3 = ListNode(15)
    p4 = ListNode(17)
    p5 = ListNode(19)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = None
    m1 = ListNode(2)
    m2 = ListNode(4)
    m3 = ListNode(6)
    m4 = ListNode(8)
    m5 = ListNode(10)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    m4.next = m5
    m5.next = None
    q1 = ListNode(12)
    q2 = ListNode(14)
    q3 = ListNode(16)
    q4 = ListNode(18)
    q5 = ListNode(20)
    q1.next = q2
    q2.next = q3
    q3.next = q4
    q4.next = q5
    q5.next = None

    s = Solution()
    test = [m1, n1, p1, q1]
    res = s.merge_k_list(test)
    while res:
        print(res.val)
        res = res.next

