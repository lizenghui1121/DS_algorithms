"""

@Author: Li Zenghui
@Date: 2020-04-05 20:37
"""
from list_node import ListNode


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        new_head = ListNode(-1)
        new_head.next = pHead
        pre = new_head
        p = pHead
        nex = None
        while p!=None and p.next!=None:
            nex = p.next
            if p.val == nex.val:
                while nex!= None and nex.val == p.val:
                    nex = nex.next
                pre.next = nex
                p = nex
            else:
                pre = p
                p = p.next
        return new_head.next

