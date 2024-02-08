import sys
from collections import deque
input=sys.stdin.readline


def bfs(by,bx):
    global answer
    #매루프마다 초기화해서 브루트포스 돌리기용 board
    board=list([0]*M for _ in range(N))
    board[by][bx]=1
    que=deque()
    que.append([by,bx])
    while que:
        y,x=que.popleft()
        for vy,vx in vector:
            my,mx=vy+y,vx+x
            if 0<=my<N and 0<=mx<M and board[my][mx]==0 and map[my][mx]=="L":
                board[my][mx]=board[y][x]+1
                que.append([my,mx])
                answer=max(answer,board[my][mx])
              


N,M=map(int,input().split())
map=list(list(input().rstrip())for _ in range(N))
vector=[[0,1],[-1,0],[1,0],[0,-1]]
answer=0
for i in range(N):
    for j in range(M):
        if map[i][j]=="L":
            bfs(i,j)
print(answer-1)
#print(*board,sep="\n")
