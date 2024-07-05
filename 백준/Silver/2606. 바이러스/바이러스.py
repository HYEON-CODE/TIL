import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
n = int(input())
m = int(input())
from collections import deque

def dfs(r):
    global count
    visited[r-1] = 1
    for x in graph[r]:
        if not visited[x-1]:
            count += 1
            visited[x-1] = 1
            dfs(x)
    return count

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
visited = [0] * (n)
result = dfs(1)
print(result)