import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# combination
# 바이러스가 있는 좌표로 3개 추르리고

# bfs로 바이러스를 돌려보고
# for문
# 돌려보고 보드에 0이 없는 경우
# max값이 min인 것을 계속 갱신


def bfs(v):
    turn = 0
    vector = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    #visited = [[0]*N for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    for vy, vx in v:
        que.append([vy, vx])
    for y, x in que:
        visited[y][x] = 0
    while que:
        y, x = que.popleft()
        for vey, vex in vector:
            my, mx = vey+y, vex+x
            if 0 <= my < N and 0 <= mx < N and board[my][mx] != 1 and visited[my][mx] == -1:
                visited[my][mx] = visited[y][x] + 1  # 몇번째 턴인지 세기위해
                que.append([my, mx])

    #print(*visited, sep="\n")
    # print("====================")
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                # 감염이 안된 곳이 있으면 1000(1000까지 올라갈 일은 없으니)
                return 1000
            else:
                # 감염이 안된 곳이 없으면 max값
                turn = max(turn, visited[i][j])
    return turn


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
que = deque()
answer = 1000


for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

# 조합으로 바이러스가 3개인 경우 탐색
for v in combinations(virus, M):
    answer = min(bfs(v), answer)


if answer == 1000:
    print(-1)
else:
    print(answer)
