"""
描述：
已知两个单词，分别为起始单词和结束单词，一个单词词典，根据转换规则，计算从起始单词到结束单词的最短转换步数。
转换规则：
1. 在转换时，只能转换单词中的一个字符；
2. 转换得到的新单词，必须在单词词典中。
条件：
1. 若无法转换，返回 0
2. 所有单词长度相同
3. 只包含小写字母
4. wordList无重复单词
5. begin_word 和 end_word 非空，且不同
@Author: Li Zenghui
@Date: 2020-04-01 14:56
"""


# 两个单词能否相连
def can_connect(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1


# 构造图
def construct_graph(begin_word, word_list, graph):
    word_list.append(begin_word)
    for item in word_list:
        graph[item] = []
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if can_connect(word_list[i], word_list[j]):
                graph[word_list[i]].append(word_list[j])
                graph[word_list[j]].append(word_list[i])


def word_ladder(begin_word, end_word, word_list):
    graph = {}
    construct_graph(begin_word, word_list, graph)
    visit = []
    q = []
    res = 0
    q.append([begin_word, 1])
    visit.append(begin_word)
    while q:
        temp = q.pop(0)
        if temp[0] == end_word:
            return temp[1]
        res += 1
        for item in graph[temp[0]]:
            if item not in visit:
                q.append([item, res])
                visit.append(item)
    return 0


if __name__ == '__main__':
    print(word_ladder('hit', 'hog', ['hot', 'lot', 'dot', 'dog', 'log', 'cog', 'hog']))
