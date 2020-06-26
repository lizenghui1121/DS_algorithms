"""

@Author: Li Zenghui
@Date: 2020-03-01 21:58
"""

s = input().split(';')
valid = 'WASD'
op = []
x = 0
y = 0
for i in s:
    if len(i) > 0 and i[0] in valid:
        if i[1:].isdigit():
            if i[0] == 'W':
                y += int(i[1:])
            if i[0] == 'S':
                y -= int(i[1:])
            if i[0] == 'A':
                x -= int(i[1:])
            if i[0] == 'D':
                x += int(i[1:])
print(str(x) + ',' + str(y))
