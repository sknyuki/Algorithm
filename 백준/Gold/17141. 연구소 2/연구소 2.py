import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

vector=[[1,0],[0,1],[-1,0],[0,-1]]
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
virus=[]
answer=float('inf')

def bfs(v):
    que=deque(v)
    max_value=0
    visited=[[-1]*N for _ in range(N)]
    for y,x in v:
        visited[y][x]=0
    while que:
        y,x=que.popleft()
        for vy,vx in vector:
            my,mx=vy+y,vx+x
            if 0<=my<N and 0<=mx<N and board[my][mx]!=1 and visited[my][mx]==-1:
                visited[my][mx]=visited[y][x]+1
                que.append([my,mx])

    for y in range(N):
        for x in range(N):
            if visited[y][x]==-1 and board[y][x]!=1:
                return float('inf')
            else:
                max_value=max(max_value,visited[y][x])
    return max_value
    

for y in range(N):
    for x in range(N):
        if board[y][x]==2:
            virus.append([y,x])

for v in list(combinations(virus,M)):
    answer=min(answer,bfs(v))

if answer==float('inf'):
    print(-1)
else:
    print(answer)