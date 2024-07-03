import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
n, m, r = map(int, input().split())
from collections import deque

def dfs(r):
    global count
    visited[r-1] = count
    result[count-1] = r
    for x in graph[r]:
        if not visited[x-1]:
            count += 1
            visited[x-1] = count
            result[count-1] = x
            dfs(x)
    return result

def bfs(r):
    visited = [0] * (n)
    queue = deque([r])
    cnt=1
    visited[r-1] = cnt
    result[cnt-1] = r
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if not visited[x-1]:
                cnt += 1
                visited[x-1] = cnt
                result[cnt-1] = x
                queue.append(x)
    print(*result[0:cnt])

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

count=1
visited = [0] * (n)
result = [0] * (m+1)
dfs(r)
print(*result[0:count])
bfs(r)