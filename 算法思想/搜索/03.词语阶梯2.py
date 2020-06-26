"""
描述：
已知两个单词，分别为起始单词和结束单词，一个单词词典，根据转换规则，计算从起始单词到结束单词的最短转换步数。
返回所有转换路径。
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
@Date: 2020-04-01 15:53
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
    has_begin_word = False
    for item in word_list:
        graph[item] = []
        if begin_word == item:
            has_begin_word = True
    graph[begin_word] = []

    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if can_connect(word_list[i], word_list[j]):
                graph[word_list[i]].append(word_list[j])
                graph[word_list[j]].append(word_list[i])
        if not has_begin_word and can_connect(begin_word, word_list[i]):
            graph[begin_word].append(word_list[i])


def bfs(begin_word, end_word, word_list):
    graph = {}
    construct_graph(begin_word, word_list, graph)
    # print(graph)
    visit = {x: 0 for x in word_list}
    # print(visit)
    end_word_pos = []
    q = []
    min_step = 0
    q.append([begin_word, -1, 1])
    front = 0
    visit[begin_word] = 1
    while front != len(q):
        temp = q[front]
        step = temp[2]
        if min_step != 0 and step > min_step:
            break
        if temp[0] == end_word:
            min_step = step
            end_word_pos.append(front)
        for item in graph[temp[0]]:
            if visit[item] == 0 or visit[item] == step+1:
                q.append([item, front, step+1])
                visit[item] = step + 1
        # print(visit)
        front += 1
    print(q)
    print('end_word_pos', end_word_pos)
    res = []
    for i in range(len(end_word_pos)):
        pos = end_word_pos[i]
        path = []
        while pos != -1:
            path.append(q[pos][0])
            pos = q[pos][1]
        res.append(path[::-1])
    return res


if __name__ == '__main__':
    print(bfs('hit', 'cog', ['hot', 'lot', 'dot', 'dog', 'log', 'cog']))
