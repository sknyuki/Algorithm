import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x, z):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[y][x][z] = 1
    #board[y][x] = 1
    que = deque()
    que.append([y, x, z])
    while que:
        y, x, z = que.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][z]
        for vy, vx in vector:
            my, mx = y+vy, x+vx
            if 0 <= my < N and 0 <= mx < M:
                if board[my][mx] == 0 and visited[my][mx][z] == 0:
                    visited[my][mx][z] = visited[y][x][z]+1
                    # print('벽미방문')
                    #print(*visited, sep="\n")
                    que.append([my, mx, z])
                    # print(que)

                if board[my][mx] == 1 and z == 1:
                    visited[my][mx][z-1] = visited[y][x][z]+1
                    # print('벽방문')
                    # print(f"x:{x},y:{y},z:{z}")
                    #print(*visited, sep="\n")
                    que.append([my, mx, z-1])
                   # print(que)
    return -1


N, M = map(int, input().split())
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
board = list(list(map(int, input().strip())) for _ in range(N))
print(bfs(0, 0, 1))
