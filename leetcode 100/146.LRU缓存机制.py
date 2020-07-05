"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

解题思路：哈希表 + 双向链表
@Author: Li Zenghui
@Date: 2020-07-04 16:31
"""


class DLinkedNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.addToHead(node)
        return node.val

    def put(self, key, val):
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, val)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 删掉最后一个元素
                remove_node = self.removeTail()
                self.cache.pop(remove_node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = val
            self.moveToHead(node)

    def addToHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    print(lru.get(3))
    print(lru.get(4))
