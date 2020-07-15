"""

@Author: Li Zenghui
@Date: 2020-07-13 21:08
"""


def removeInvalidParentheses( s):
    def is_valid(s):
        cnt = 0;
        for c in s:
            if c == '(':
                cnt += 1
            if c == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    q = {s}
    while q:
        valid_list = list(filter(is_valid, q))
        if valid_list:
            return valid_list
        next_q = set()

        for item in q:
            for i in range(len(item)):
                if item[i] in '()':
                    next_q.add(item[:i] + item[i + 1:])
        q = next_q


if __name__ == '__main__':
    s = '()))()'
    print(removeInvalidParentheses(s))