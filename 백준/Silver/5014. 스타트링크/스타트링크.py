import sys
from collections import deque
input=sys.stdin.readline

#일단 [0]*F의 리스트를 생성
#bfs(S)로 함수 시작
#방문 처리를 해주면서+1
#board의 G위치에 수치가 채워지면return board[G]
#루프를 다 돌아도 답이 안나오면 return "use the stairs"

def bfs(S):
    que=deque()
    que.append(S)
    board[S]=1
    while que:
        now=que.popleft()
        #print(board)
        if board[G]!=0:#내부에 값이 채워지면
            return board[G]-1
        for vx in vector:
            next=now+vx
            if 1<=next<=F and board[next]==0:
                que.append(next)
                board[next]=board[now]+1
    return "use the stairs"



F,S,G,U,D=map(int,input().split())
vector=[U,-D]
board=[0]*(F+1)
print(bfs(S))
