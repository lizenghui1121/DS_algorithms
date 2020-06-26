"""
已知N组括号，生成这N组括号的所有合法可能
@Author: Li Zenghui
@Date: 2020-04-06 15:10
"""


# 递归生成所有可能,包括合法不合法
def gen_test(n):
    def generate(item, n, result):
        if len(item) >= 2 * n:
            result.append(item)
            return

        generate(item + '(', n, result)
        generate(item + ')', n, result)

    res = []
    generate("", n, res)
    return res


def gen_test_2(n):
    def backtrack(q, i, track, res):
        if i == 2 * q:
            res.append(''.join(track))
            return
        for item in ["(", ')']:
            track.append(item)
            backtrack(q, i+1, track, res)
            track.pop()
    track = []
    res = []
    backtrack(n, 0, track, res)
    return res


def generate_parentheses(n):
    def generate(item, left, right, result):
        if left == 0 and right == 0:
            result.append(item)
            return
        if left > 0:
            generate(item + '(', left - 1, right, result)
        if left < right:
            generate(item + ')', left, right - 1, result)

    start = ''
    res = []
    generate(start, n, n, res)
    return res

def generate_parentheses_2(n):
    def back_track(track, left, right, res):
        if left == 0 and right == 0:
            res.append(''.join(track))
        if left > 0:
            track.append('(')
            back_track(track, left-1, right, res)
            track.pop()
        if left < right:
            track.append(')')
            back_track(track, left, right-1, res)
            track.pop()
    track = []
    res = []
    back_track(track, n, n, res)
    return res


if __name__ == '__main__':
    # print(gen_test(2))
    print(gen_test_2(2))
    print(generate_parentheses(2))
    print(generate_parentheses_2(2))
