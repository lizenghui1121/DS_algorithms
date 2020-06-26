"""

@Author: Li Zenghui
@Date: 2020-03-11 15:10
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


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
    while head:
        print(head.val)
        head = head.next
