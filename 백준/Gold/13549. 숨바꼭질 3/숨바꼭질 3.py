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
        for i in (a-1, a+1, a*2):
            if 0 <= i <= 100000 and time[i] == 0:
                if i == a*2:
                    time[i] = time[a]
                    que.appendleft(i)  # 순간이동은 소요시간 0초이기에 우선순위가 나머지 2개보다 높음
                else:
                    time[i] = time[a]+1
                    que.append(i)


N, K = map(int, input().split())
time = [0]*(100001)
bfs(N, K)
