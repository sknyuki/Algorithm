import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x, eyes, qc):
    vector = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    que = deque()
    que.append([y, x])
    visited[y][x] = True
    # normal
    if eyes == 'normal':
        while que:
            y, x = que.popleft()
            for vy, vx in vector:
                my, mx = vy+y, vx+x
                if 0 <= my < N and 0 <= mx < N and board[my][mx] == qc and not visited[my][mx]:
                    visited[my][mx] = True
                    que.append([my, mx])
        major[qc] += 1
    # minor
    elif eyes == "minor":
        while que:
            y, x = que.popleft()
            for vy, vx in vector:
                my, mx = vy+y, vx+x
                if 0 <= my < N and 0 <= mx < N and not visited[my][mx]:
                    if board[my][mx] == qc == "B":
                        visited[my][mx] = True
                        que.append([my, mx])
                    elif board[my][mx] != "B" and qc != "B":
                        visited[my][mx] = True
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

# for normal
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 'normal', board[i][j])


visited = [[False]*N for _ in range(N)]

# for minor
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 'minor', board[i][j])


print(sum(major.values()))
print(sum(minor.values()))
