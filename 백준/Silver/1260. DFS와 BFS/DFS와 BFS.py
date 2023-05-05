import sys
from collections import deque
input = sys.stdin.readline


def DFS(n):
    visited1[n] = True
    print(n, end=" ")
    for j in graph[n]:
        if not visited1[j]:
            DFS(j)


def BFS(n):
    que = deque()
    visited2[n] = True
    que.append(n)
    while que:
        a = que.popleft()
        print(a, end=" ")
        for i in graph[a]:
            if not visited2[i]:
                que.append(i)
                visited2[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i].sort()


visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

DFS(V)
print()
BFS(V)
