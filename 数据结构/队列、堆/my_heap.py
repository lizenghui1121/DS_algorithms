"""

@Author: Li Zenghui
@Date: 2020-03-22 11:49
"""

class MyHeap:

    def __init__(self, elist):
        self.elems = list(elist)
        if self.elems:
            self.build_heap()

    def is_empty(self):
        return not self.elems

    # 取堆顶元素
    def peek(self):
        if self.is_empty():
            raise ValueError('堆为空！')
        return self.elems[0]

    # 建立堆
    def build_heap(self):
        n = len(self.elems)
        for i in reversed(range(n//2)):
            self.siftup(self.elems, i)
    # 上浮
    def siftup(self,heap, pos):
        end_pos = len(heap)
        start_pos = pos
        new_item = heap(start_pos)
        child_pos = 2 * pos + 1
        while child_pos < end_pos:
            right_pos = child_pos + 1
            if right_pos < end_pos and heap[right_pos] < heap[child_pos]:
                child_pos = right_pos
            if new_item < heap[right_pos]:
                break
            heap[pos] = heap[right_pos]
            pos = right_pos
            child_pos = 2 * pos + 1
        heap[pos] = heap[start_pos]



