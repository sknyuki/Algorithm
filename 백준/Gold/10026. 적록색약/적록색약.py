import sys
from collections import deque
input = sys.stdin.readline
# 단지 번호 붙이기와 유사
# dict{'R':0 ,'B':0 ,'G':0 }
# for문 돌리며 R,B,G가 나올 때까지 탐색 탐색된 point로 bfs([y,x,qc])시작

# 적록색약 & 노말 함수 따로 만들어서 visited처리로 board를 재활용


def bfs(y, x, qc):
    vector = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    que = deque()
    que.append([y, x])
    visited[y][x] = True
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < N and 0 <= mx < N and board[my][mx] == qc and not visited[my][mx]:
                visited[my][mx] = True
                que.append([my, mx])
    major[qc] += 1


def bfs_blind(y, x, qc):
    vector = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    que = deque()
    que.append([y, x])
    visited[y][x] = False
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < N and 0 <= mx < N and visited[my][mx]:
                if board[my][mx] == qc == "B":
                    visited[my][mx] = False
                    que.append([my, mx])
                elif board[my][mx] != "B" and qc != "B":
                    visited[my][mx] = False
                    que.append([my, mx])

    if qc == "B":
        minor['B'] += 1
    else:
        minor['R&G'] += 1


N = int(input())
board = [list(input().strip())for _ in range(N)]
major = {'R': 0, 'B': 0, 'G': 0}
minor = {'R&G': 0, 'B': 0}
visited = [[False]*N for _ in range(N)]

#for normal
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, board[i][j])
           
#for minor
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            bfs_blind(i, j, board[i][j])


print(sum(major.values()))
print(sum(minor.values()))
