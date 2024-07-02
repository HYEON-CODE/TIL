import sys
sys.setrecursionlimit(150000)

def dfs(r):
    global cnt
    visited[r] = cnt
    cnt += 1 
    graph[r].sort(reverse=True)
    for x in graph[r]:
        if not visited[x]:
            dfs(x)       
    return visited


n, m ,r = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
result = dfs(r)
for i in range(1, len(result)):
    if result[i]:
        print(result[i])
    else:
        print(0)