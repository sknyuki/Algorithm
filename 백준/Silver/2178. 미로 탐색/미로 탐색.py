import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x):
    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    que = deque()
    que.append([y, x])
    while que:
        y, x = que.popleft()
        for vy, vx in vector:
            if 0 <= vy+y < N and 0 <= vx+x < M and graph[y+vy][x+vx] == 1 :
                graph[y+vy][x+vx] = graph[y][x]+1
                que.append([y+vy, x+vx])


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]


bfs(0, 0)
#print(*graph, sep="\n")
print(graph[N-1][M-1])
