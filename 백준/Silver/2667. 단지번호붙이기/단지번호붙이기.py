import sys
from collections import deque
input = sys.stdin.readline
# 설계
# while True: 0,0 시작 이중 for문으로 1이있는 위치 탐색
# if maze[ny][nx] == 1 :
#   while maze[ny][nx]!=0 이동하면서  maze[ny][nx]=0로 변환& cnt+1--> 이동못하게 되면 단지하나끝

# 위 과정 반복

def bfs(y, x):
    vector = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    que = deque()
    que.append([y, x])
    list_map[y][x] = 0
    cnt = 1
    while que:  # BFS로 건물 탐색
        y, x = que.popleft()
        for vy, vx in vector:
            if 0 <= y+vy < N and 0 <= x+vx < N and list_map[y+vy][x+vx] == 1:
                list_map[y+vy][x+vx] = 0  # 탐색이 끝난 건물은 다시 세는일 없도록 철거
                cnt += 1
                que.append([y+vy, x+vx])
    cnt_list.append(cnt)


N = int(input())
list_map = list(list(map(int, input().strip())) for _ in range(N))
cnt_list = []


for i in range(N):
    for j in range(N):
        if list_map[i][j] == 1:
            bfs(i, j)

cnt_list.sort()
print(len(cnt_list))
print(*cnt_list, sep="\n")
