

t = int(input())
for _ in range(t):
    s = input()
    q = [(s, 0)]
    visted = set()
    while q:
        cur, step = q.pop(0)
        if "0010" not in cur:
            print(step)
            break
        target_index = cur.index("0010")
        for i in range(target_index, target_index + 4):
            new_str = cur[:i] + cur[i+1:]
            if new_str not in visted:
                q.append((new_str, step + 1))
                visted.add(new_str)


