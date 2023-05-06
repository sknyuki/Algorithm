import sys
from collections import deque
input = sys.stdin.readline


def BFS(N):
    visited[N] = True
    que = deque()
    que.append(N)
    while que:
        a = que.popleft()
        infested.append(a)
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                que.append(i)


N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in graph:
    i.sort()

visited = [False]*(N+1)
infested = []
BFS(1)

print(len(infested)-1)
