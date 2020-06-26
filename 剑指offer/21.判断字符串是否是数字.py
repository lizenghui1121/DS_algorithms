"""

@Author: Li Zenghui
@Date: 2020-04-05 19:47
"""


def is_number(s):
    try:
        float(s)
        return True
    except:
        return False


if __name__ == '__main__':
    print(is_number('12-4'))
