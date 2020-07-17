"""

@Author: Li Zenghui
@Date: 2020-07-17 14:47
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def getIntersectionNode(headA, headB):
    def getLength(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    l1 = getLength(headA)
    l2 = getLength(headB)
    if l1 > l2:
        gap = l1 - l2
        while gap > 0:
            headA = headA.next
            gap -= 1
    if l2 > l1:
        gap = l2 - l1
        while gap > 0:
            headB = headB.next
            gap -= 1
    while headA:
        if headA == headB:
            return headA
        headB = headB.next
        headA = headA.next
    return None


if __name__ == '__main__':
    n0 = ListNode(5)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(2)
    m1 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    m1.next = n2
    getIntersectionNode(n0, m1)