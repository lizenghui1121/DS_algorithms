
n = int(input())

def f(n):
    q = [(n, 0)]
    s = set()
    while q:
        val, step = q.pop(0)
        for i in range(n):
            new_val = val - i * i
            if new_val < 0:
                break
            if new_val == 0:
                return step + 1
            if new_val not in s:
                q.append((new_val, step + 1))
                s.add(new_val)
    return -1

print(f(n))
