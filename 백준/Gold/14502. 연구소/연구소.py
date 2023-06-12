import sys
from collections import deque
input = sys.stdin.readline

# 바이러스가 퍼지는 로직
# bfs로 바이러스 퍼지는거 구현

# 벽을 3개 랜덤으로 세워가는거 (브루트포스)
# 백트레킹으로 벽3개 칠하는거 구현

# 다 퍼져나간후 살아남은 0의 갯수를 max로 최신화
#-> 전체영역-오염된 영역의 max값 


# 벽 함수
def MakeWall(wall):
    global reslut
    if wall == 3:  # 벽이 3개 완성 되면 바이러스 함수 실행
        DeadArea = bfs()
        # 전체에서 오염된 땅 뺀 값의 최댓값
        reslut = max(reslut, (Y*X)-DeadArea)
        return

    for y in range(Y):
        for x in range(X):
            if board[y][x] == 0:
                board[y][x] = 1
                MakeWall(wall+1)
                board[y][x] = 0
# 감염 함수
def bfs():
    que = deque()
    DeadArea = 0
    visited = [[0]*X for _ in range(Y)]
    for y in range(Y):
        for x in range(X):
            if board[y][x] != 0:
                DeadArea += 1 #순환 이전 오염된 영역
            if board[y][x] == 2:
                que.append([y, x])
    vector = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < Y and 0 <= mx < X and board[my][mx] == 0 and visited[my][mx] == 0:
                visited[my][mx] = 3
                que.append([my, mx])

    for i in visited:#순환 이후 오염된 영역
        DeadArea += i.count(3)
    return DeadArea


Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
wall = 0
reslut = 0



# 벽 짓기 & 바이러스
MakeWall(wall)

print(reslut)

