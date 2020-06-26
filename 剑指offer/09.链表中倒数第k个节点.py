"""
输出链表中倒数第K个节点
@Author: Li Zenghui
@Date: 2020-03-03 16:06
"""


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k==0:
            return None
        length = 0
        r = head
        while r:
            r = r.next
            length += 1
        if k > length:
            return None
        p = head
        q = head
        for i in range(k-1):
            q = q.next
        while q.next is not None:
            p = p.next
            q = q.next
        return p


class Solution2:
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head!=None:
            l.append(head)
            head=head.next
        if k>len(l) or k<1:
            return
        return l[-k]


