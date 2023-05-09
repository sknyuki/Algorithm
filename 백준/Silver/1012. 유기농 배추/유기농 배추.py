import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


def bfs(x, y):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque()
    graph[x][y] = 0
    cnt = 1
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for vy, vx in vector:
            if 0 <= x+vx < N and 0 <= y+vy < M and graph[x+vx][y+vy] == 1:
                graph[x+vx][y+vy] = 0
                cnt += 1
                que.append([x+vx, y+vy])
    cnt_list.append(cnt)


len_cnt_list = []

for i in range(T):
    cnt_list = []
    M, N, K = map(int, input().split())
    graph = [[0]*M for i in range(N)]
    for j in range(K):
        A, B = map(int, input().split())
        graph[B][A] = 1
    for y in range(M):
        for x in range(N):
            if graph[x][y] == 1:
                bfs(x, y)
    print(len(cnt_list))
