st = input()
result = set()
for i in range(len(st)):
    for j in range(i, len(st)):
        result.add(st[i:j+1])

print(len(result))