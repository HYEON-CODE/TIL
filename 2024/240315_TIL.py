# 왕실의 나이트
n = list(input())
x, y = (ord(n[0])-96), int(n[1])
result = 0
steps = [(-2, -1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    result += 1
print(result)