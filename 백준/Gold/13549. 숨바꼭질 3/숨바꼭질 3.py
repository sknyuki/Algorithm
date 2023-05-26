import sys
from collections import deque
input = sys.stdin.readline


def bfs(N, K):
    que = deque()
    que.append(N)
    time[N] = 1
    while que:
        a = que.popleft()
        if a == K:
            print(time[a]-1)
            break
        for i in (a*2,a-1, a+1):# a*2를 제일 앞에 배치 하여 우선적으로 계산하도록함 
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
