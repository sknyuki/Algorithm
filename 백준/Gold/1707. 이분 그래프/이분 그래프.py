import sys
from collections import deque
input = sys.stdin.readline


def bfs(N):
    visited[N] = 1
    que = deque()
    que.append(N)
    while que:
        a = que.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = -visited[a]
                que.append(i)
            else:
                if visited[i] == visited[a]:  # 이전항과 같이 같으면 안되기에 False 반환
                    return False
    return True  # 다 돈 이후 문제 없으면 True반환


N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    graph = [[]for _ in range(A)]
    visited = [0]*(A)
    for _ in range(B):
        C, D = map(int, input().split())
        graph[C-1].append(D-1)
        graph[D-1].append(C-1)

    result = "YES"
    for i in range(A):
        if not visited[i]:
            if not bfs(i):
                result = "NO"
    print(result)
