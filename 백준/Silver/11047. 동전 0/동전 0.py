n, k = map(int, input().split())
coins = list()
result = 0
for _ in range(n):
    coins.append(int(input()))
for i in range(1, n+1):
    if k // coins[-i]!=0:
        result += k // coins[-i]
        k = k%coins[-i]
print(result)