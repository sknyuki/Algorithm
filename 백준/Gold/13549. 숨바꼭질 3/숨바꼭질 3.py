import sys
from collections import deque
input = sys.stdin.readline


def bfs(N, K):
    que = deque()
    que.append(N)
    while que:
        a = que.popleft()
        if a == K:
            print(time[a])
            break
        for i in (a*2,a-1, a+1):
            if 0 <= i <= 100000 and time[i] == 0:
                if i == a*2:
                    time[i] = time[a]
                    que.append(i)  
                else:
                    time[i] = time[a]+1
                    que.append(i)


N, K = map(int, input().split())
time = [0]*(100001)
bfs(N, K)
