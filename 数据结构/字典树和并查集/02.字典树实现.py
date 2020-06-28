"""
python 实现字典树insert，search，startsWith
@Author: Li Zenghui
@Date: 2020-06-28 22:17
"""
from collections import defaultdict


class TireNode:
    def __init__(self):
        self.node = defaultdict(TireNode)  # dict的value是TireNode对象而不是字符
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            cur = cur.node[w]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w in cur.node:
                cur = cur.node[w]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p in cur.node:
                cur = cur.node[p]
            else:
                return False
        return True
