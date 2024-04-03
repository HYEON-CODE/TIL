n = int(input())
top = list(map(int, input().split()))
result = [] # 결과 인덱스 저장하는 곳
high = [] # 레이저 신호를 수신한 탑들의 인덱스를 저장하는 스택

for i in range(n):
    while high:
        if top[high[-1]] < top[i]:
            high.pop()
        else:
            result.append(high[-1]+1)
            break
    else:
        result.append(0)

    high.append(i)

print(*result)