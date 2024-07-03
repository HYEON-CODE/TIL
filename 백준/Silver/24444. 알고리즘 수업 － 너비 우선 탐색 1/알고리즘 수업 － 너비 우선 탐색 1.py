import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
n, m, r = map(int, input().split())
from collections import deque

def bfs(r):
    queue = deque([r])
    cnt = 1
    visited[r-1] = cnt
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v-1]:
                cnt += 1
                visited[v-1] = cnt
                queue.append(v)


visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

bfs(r)
for i in range(n):
    print(visited[i])