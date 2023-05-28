import sys
from collections import deque
input = sys.stdin.readline


def Pozack(n):
    que = deque()
    que.append(n)
    while que:
        now = que.popleft()
        if now == K:
            print(visited[now])
            temp = now
            result = []
            for _ in range(visited[now]+1):# 이동횟수 만큼
                result.append(temp)  # 출력 할 최종위치값 넣고
                temp = rode[temp]  # 해당 위치로 이동해서 저장된 이전의 위치 값을 temp저장
            print(*result[::-1])  # 역순으로 출력
            return
        for next in (now-1, now+1, now*2):
            if 0 <= next < Max and not visited[next]:
                visited[next] = visited[now]+1  # 이동 좌표+1
                rode[next] = now  # 지나갈 경로에 이전의 위치값 저장
                que.append(next)


N, K = map(int, input().split())
Max = 100001
visited = [0]*Max
rode = [0]*Max  # 경로 탐색을 위한 list

if N == K:
    print(0)
    print(N)
elif N > K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=" ")
else:
    Pozack(N)
