import sys
from collections import deque
input = sys.stdin.readline

# visited를 3차원으로 설정
# visited[y][x][1]에 기록이 되면 벽을 아직 안 뚫은 상태의 이동횟수
# visited[y][x][0]에 기록이 되면 벽을 뚫은 상태의 이동횟수

def bfs(y, x, z):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[y][x][z] = 1  # 초기 위치(벽 파괴전)
    que = deque()
    que.append([y, x, z])
    while que:
        y, x, z = que.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][z]
        for vy, vx in vector:
            my, mx = y+vy, x+vx
            if 0 <= my < N and 0 <= mx < M:
                # 벽이 아닐때
                if board[my][mx] == 0 and visited[my][mx][z] == 0:
                    visited[my][mx][z] = visited[y][x][z]+1
                    que.append([my, mx, z])
                # 벽일 때
                elif board[my][mx] == 1 and z == 1:  # 벽과 마주했으며, 아직 벽을 파괴할 수 있을때
                    visited[my][mx][z-1] = visited[y][x][z] + \
                        1  # 벽과 마주하기 전항의 +1 만큼 z-1(0)에 기록
                    que.append([my, mx, z-1])
    return -1 # queue다 돌아버리면 -1반환


N, M = map(int, input().split())
board = list(list(map(int, input().strip())) for _ in range(N))
visited = list(list([0]*2 for _ in range(M)) for _ in range(N))

print(bfs(0, 0, 1))
