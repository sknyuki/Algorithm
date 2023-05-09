import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

#단지문제와 동일

def bfs(y, x):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque()
    graph[y][x] = 0
    cnt = 1
    que.append([y, x])
    while que:    #루틴을 돌며 인접한 배추의 수를 세어줌
        y, x = que.popleft()
        for vy, vx in vector:
            if 0 <= x+vx < M and 0 <= y+vy < N and graph[y+vy][x+vx] == 1:
                graph[y+vy][x+vx] = 0
                cnt += 1
                que.append([y+vy, x+vx])
    cnt_list.append(cnt)



len_cnt_list = []

for i in range(T):
    cnt_list = []
    M, N, K = map(int, input().split())
    graph = [[0]*M for i in range(N)]
    for j in range(K):
        A, B = map(int, input().split())
        graph[B][A] = 1    #그래프작성
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:    #그래프 내부 1을 찾음 BFS의 시작점 탐색
                bfs(y, x)
    print(len(cnt_list))
