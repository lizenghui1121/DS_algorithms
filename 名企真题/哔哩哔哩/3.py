
version = input().replace("[", "").replace(']', "").replace("\"", "").split(",")
print(sorted(version, key=lambda x: tuple(int(v) for v in x.split("."))))
