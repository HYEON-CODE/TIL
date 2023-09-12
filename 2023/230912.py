#BOJ 10811번: 바구니 뒤집기
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
for ball in basket:
    print(ball, end=' ')
# 간단한 문제인데 시간을 많이 소모했다.
# 파이썬 백슬라이싱에 대해 오해했던 게 많이 풀렸다.
