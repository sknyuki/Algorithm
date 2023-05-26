import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x):
    vector = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[0]*X for _ in range(Y)]
    visited[y][x] = 1
    que = deque()
    que.append([y, x])
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            my, mx = vy+y, vx+x
            if 0 <= my < Y and 0 <= mx < X and board[my][mx] == "L" and visited[my][mx] == 0:
                visited[my][mx] = visited[y][x]+1
                que.append([my, mx])
   # print(*visited, sep="\n")
    return visited[y][x]-1


Y, X = map(int, input().split())
board = [list(input().strip()) for _ in range(Y)]
max_value = 0

# 'L'마다 탐색
# -> return되는 visited(최종 이동거리값)을 max_value에 저장
for i in range(Y):
    for j in range(X):
        if board[i][j] == "L":
            max_value = max(max_value, bfs(i, j))

# max값 출력
print(max_value)
