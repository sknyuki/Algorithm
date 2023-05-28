import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, way):
    que = deque()
    que.append([n, way])
    visited[n] = 1
    while que:
        now, way = que.popleft()
        way = way+[now] 
        # print(que)
        if now == K:
            print(visited[now]-1)
            print(*way, sep=" ")
            return
        for next in (now-1, now+1, now*2):
            if 0 <= next < Max and not visited[next]:
                visited[next] = visited[now]+1
                que.append([next, way])


N, K = map(int, input().split())
Max = 100001
visited = [0]*Max
ways = []

if N == K:
    print(0)
    print(N)
elif N > K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=" ")
else:
    bfs(N, ways)
