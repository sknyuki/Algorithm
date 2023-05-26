import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]

vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]

D=0
cnt=0
y,x=0,0
board[0][0]=1
for i in range(N*M):
    ny,nx=y+vector[D][0],x+vector[D][1]
    if 0<=ny<N and 0<=nx<M and board[ny][nx]==0:
            board[ny][nx]=1
            y,x=ny,nx
    else:
        D=(D+1)%4
        cnt+=1
        y,x=y+vector[D][0],x+vector[D][1]
        board[y][x]=1
        
                
print(cnt-1)
        