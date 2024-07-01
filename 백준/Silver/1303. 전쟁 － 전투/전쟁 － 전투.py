from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(input()) for _ in range(m)]
visited=[[False]*n for _ in range(m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,color):
    cnt=1
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==color and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    return cnt
white,blue=0,0
for i in range(m):
    for j in range(n):
        if graph[i][j]=='W' and not visited[i][j]:
            white+=bfs(i,j,'W')**2
        elif graph[i][j]=='B' and not visited[i][j]:
            blue+=bfs(i,j,'B')**2
print(white,blue)