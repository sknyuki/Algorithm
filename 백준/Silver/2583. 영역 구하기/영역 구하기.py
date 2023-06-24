import sys
from collections import deque
input=sys.stdin.readline

#각 사각형들을 -1로 표시 -1이 아닌 부분들을 for문을 돌며 탐색

def bfs(y,x):
    vector=[[0,1],[1,0],[-1,0],[0,-1]]
    que=deque()
    que.append([y,x])
    board[y][x]=1# 1부터 시작
    cnt_value=1
    while que:
        y,x=que.popleft()
        for vy,vx in vector:
            my,mx=vy+y,vx+x
            #print(my,mx)
            if 0<=my<M and 0<=mx<N and board[my][mx]==0:
                board[my][mx]=board[y][x]+1
                que.append([my,mx])
                cnt_value+=1#몇번을 탐색하였는지
    return cnt_value


M,N,K=map(int,input().split())
board=[[0]*N for _ in range(M)]
cnt=0
answer_list=[]
#각 사각형들을 칠하고
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j]=-1
        
#0인 부분이 있으면 탐색
for y in range(M):
    for x in range(N):
        if board[y][x]==0:
            answer_list.append(bfs(y,x))#정답list return
            cnt+=1#빈 공간블록이 몇개있는지

answer_list.sort()
print(cnt)
print(*answer_list, sep=" ")
