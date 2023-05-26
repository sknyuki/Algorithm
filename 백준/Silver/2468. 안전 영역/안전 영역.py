import sys
from collections import deque
input = sys.stdin.readline
# 0부터 max(board) 까지 수위를 올려가며 안전영역의 갯수를 탐색
# 탐색된 cnt 의 갯수를 list에 append해줘가며 max값을 출력


def bfs(y, x, rain):
    vector = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    visited[y][x] = True
    que = deque()
    que.append([y, x])
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < N and 0 <= mx < N and not visited[my][mx] and board[my][mx] > rain:
                visited[my][mx] = True
                que.append([my, mx])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
rain_list = []
safe_area = []
# board 내부의 max_rain값 탐색
for i in board:
    rain_list.append(max(i))
max_rain = max(rain_list)
# 비가 내릴수 있는 높이 max_rain까지 for문으로 안전구역 갯수 탐색
for rain in range(1, max_rain):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] > rain and not visited[y][x]:
                bfs(y, x, rain)
                cnt += 1
    safe_area.append(cnt)

if safe_area:
    print(max(safe_area))
else:
    print(1)
