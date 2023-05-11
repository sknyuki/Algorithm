import sys
from collections import deque
input = sys.stdin.readline

# 3차원이라고 하여도 결국에 que는 하나일것으로 예상
# 2차원 A*B 3차원 (A*B)*C

def bfs():
    vector = [[0, 0, 1], [0, 1, 0], [0, 0, -1],
              [0, -1, 0], [1, 0, 0], [-1, 0, 0]]  # 3차원 백터
    while que:
        h, y, x = que.popleft()
        for vh, vy, vx in vector:
            nh, ny, nx = h+vh, y+vy, x+vx
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and boxs[nh][ny][nx] == 0:
                boxs[nh][ny][nx] = boxs[h][y][x]+1
                que.append([nh, ny, nx])


M, N, H = map(int, input().split())
boxs = []
que = deque()

#그래프 생성#
for _ in range(H):
    box = []
    for _ in range(N):
        S = list(map(int, input().split()))
        box.append(S)
    boxs.append(box)
#print(*boxs, sep="\n")

#좌표찾기#
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxs[h][n][m] == 1:
                que.append([h, n, m])

# 함수 실행
bfs()
#답 출력
max_value = 0
for h in range(H):
    for y in range(N):
        for x in range(M):
            if boxs[h][y][x] > max_value:
                max_value = boxs[h][y][x]
            if boxs[h][y][x] == 0:
                print(-1)
                exit(0)
print(max_value-1)
