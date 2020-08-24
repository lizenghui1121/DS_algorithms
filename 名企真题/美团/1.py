

def check(name):
    if len(name) < 2 or len(name) > 20:
        return False
    if not name[0].isalpha():
        return False
    al_count = 0
    num_count = 0
    for c in name:
        if not c.isalnum():
            return False
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            al_count += 1
        if '0' <= c <= '9':
            num_count += 1
    return al_count >= 1 and num_count >= 1

t = int(input())

for _ in range(t):
    name = input()
    if check(name):
        print("Accept")
    else:
        print("Wrong")
