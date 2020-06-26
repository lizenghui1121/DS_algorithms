"""
两个有序链表的合并
@Author: Li Zenghui
@Date: 2020-03-11 21:34
"""

from list_node import ListNode


# 两个有序链表的合并
def merge_list(head_a, head_b):
    pa = head_a
    pb = head_b
    pre = ListNode(-1)
    new_head = pre
    while pa and pb:
        if pa.val > pb.val:
            pre.next = pb
            pb = pb.next
        else:
            pre.next = pa
            pa = pa.next
        pre = pre.next
    if pa:
        pre.next = pa
    if pb:
        pre.next = pb
    return new_head.next


# 多个有序链表的合并
def merge_many_list(list_arr):
    if len(list_arr) == 0:
        return None
    if len(list_arr) == 1:
        return list_arr[0]
    if len(list_arr) == 2:
        return merge_list(list_arr[0], list_arr[1])

    mid = len(list_arr)//2
    n1 = merge_many_list(list_arr[:mid])
    n2 = merge_many_list(list_arr[mid:])

    return merge_list(n1, n2)


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

    # res = merge_list(n1, m1)
    # while res:
    #     print(res.val)
    #     res = res.next
    test = [m1, n1, p1, q1]
    res = merge_many_list(test)
    while res:
        print(res.val)
        res = res.next
