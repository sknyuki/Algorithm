import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while que:
        #print("=========================")
        #print(*box, sep="\n")
        y, x = que.popleft()
        for vy, vx in vector:
            ny, nx = vy+y, vx+x
            if 0 <= ny < B and 0 <= nx < A and box[ny][nx] == 0:
                box[ny][nx] = box[y][x]+1
                que.append([ny, nx])


A, B = map(int, input().split())
box = []
que = deque()
zero = 0
for i in range(B):
    row = list(map(int, input().split()))
    box.append(row)


for i in range(B):
    for j in range(A):
        if box[i][j] == 1:
            que.append([i, j])  # 스타트점이 여러개일수도 있으니 bfs외부에서 que에 값을 넣어줌
        elif box[i][j] == 0:
            zero += 1
if zero == 0:  # 토마토가 내부에 없으면 함수 돌것도없이 바로 0 출력후 종료
    print(0)
    exit(0)

bfs()

for i in range(B):
    for j in range(A):
        if box[i][j] == 0:  # 함수를 다 돌았으나 안 익은 토마토가 남아있으면 -1출력 후 종료
            print(-1)
            exit(0)

max = max(map(max, box))  # 이차함수 최댓값 출력
print(max-1)  # 스타트가 1 이기에 -1해줌
