import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

N, M, R = map(int, input().split())

def dfs(v,depth):
    visited[v]=depth

    for i in graph[v]:
        if visited[i]==-1:
            dfs(i,depth+1)
    return

graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

dfs(R,0)

for i in range(1, N+1):
    print(visited[i])