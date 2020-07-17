"""

@Author: Li Zenghui
@Date: 2020-07-17 12:26
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    s1 = []
    s2 = []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    carry = 0
    pre = None
    while s1 or s2:
        a = s1.pop() if s1 else 0
        b = s2.pop() if s2 else 0
        ans = a + b + carry
        carry = ans // 10
        cur = ans % 10
        temp_node = ListNode(cur)
        temp_node.next = pre
        pre = temp_node
    if carry > 0:
        temp_node = ListNode(carry)
        temp_node.next = pre
        pre = temp_node
    return pre


def addTwoNumbers(l1, l2):
    if not l1 and not l2:
        return
    if not l1:
        carry = addTwoNumbers(l1, l2.next)
    if not l2:
        carry = addTwoNumbers(l1.next, l2)



if __name__ == '__main__':
    n0 = ListNode(5)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(2)
    m1 = ListNode(4)
    m2 = ListNode(6)
    m3 = ListNode(5)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    m1.next = m2
    m2.next = m3
    node = addTwoNumbers(n0, m1)
    while node:
        print(node.val)
        node = node.next