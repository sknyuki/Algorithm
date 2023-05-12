import sys
from collections import deque
input = sys.stdin.readline

# 게임판 작성
# dict로 뱀과 사다리 좌표를 설정
# 주사위dice로 1~6까지 for문 작성
# 이동된 칸을 queue에 추가
# borad==100이면 stop


def bfs(N):
    que = deque()
    que.append(N)
    while que:
        a = que.popleft()
        if a == 100:
            return board[a]  # 100일경우 return
        for dice in range(1, 7):  # 주사위
            da = a+dice
            if da <= 100 and not visited[da]:  # 기존위치+다이스의 값이 100이하일 때만
                if da in yachaL.keys():  # 사다리에 도착했을때
                    da = yachaL[da]

                if da in yachaS.keys():  # 뱀에 만났을떄
                    da = yachaS[da]

                if not visited[da]:# 뱀이나 사다리 타고 이동했을때의 값이 visited인지 다시한번 확인
                    visited[da] = True
                    board[da] = board[a]+1 
                    que.append(da)


S, L = map(int, input().split())
yachaS = dict()
yachaL = dict()
board = [0]*(101)
visited = [False]*(101)
for i in range(S):
    A, B = map(int, input().split())
    yachaS[A] = B
for i in range(L):
    A, B = map(int, input().split())
    yachaL[A] = B
#print(*board, sep="\n")
# print(yachaS)
# print(yachaL)
print(bfs(1))
