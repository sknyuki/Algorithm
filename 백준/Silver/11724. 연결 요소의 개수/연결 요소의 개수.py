import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    visited[n] = 1
    queue = deque()
    queue.append(n)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = visited[a] + 1
                queue.append(i)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(len(graph)):
    graph[i].sort()

result = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        result += 1
print(result)
