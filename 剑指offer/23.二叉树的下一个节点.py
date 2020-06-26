"""

@Author: Li Zenghui
@Date: 2020-04-05 20:59
"""


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None


