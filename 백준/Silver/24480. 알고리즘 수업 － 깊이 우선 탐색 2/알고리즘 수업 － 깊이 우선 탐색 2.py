import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(N):
    global cnt
    cnt += 1
    visited[N] = True
    result[N] = cnt
    for i in graph[N]:
        if not visited[i]:
            DFS(i)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in graph:
    i.sort(reverse=True)

visited = [False]*(N+1)
result = [0]*(N+1)
cnt = 0
DFS(R)
for i in range(1, len(result)):
    print(result[i])
