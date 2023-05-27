import sys
from collections import deque
input = sys.stdin.readline

# 언니의 위치가 동생의 위치와 같거나 앞에있을때는 따로 처리
# 언니가 뒤에있을때만 bfs사용

# 리스트 way와 리스트 visited 2개 사용
# visited는 이동 횟수 ways는 가지수
# 언제 que.append 해줄지 고민필요


def bfs(n):
    que = deque()
    que.append(n)
    locate[n] = 1
    ways[n] = 1
    while que:
        now = que.popleft()
        for next in (now-1, now+1, now*2):
            if 0 <= next < Max:

                if not locate[next]:  # 처음 방문했을때
                    que.append(next)  # 처음 방문하였을때만 que에 추가
                    locate[next] = locate[now]+1
                    ways[next] += ways[now]  #가지수+

                elif locate[next] == locate[now]+1:  # 최단시간으로 재방문했을때
                    ways[next] += ways[now]

    locate[K] -= 1


N, K = map(int, input().split())
Max = 200001
locate = [0]*Max
ways = [0]*Max

if K < N:
    print(abs(K-N))
    print(1)
elif K == N:
    print(0)
    print(1)
else:
    bfs(N)
    print(locate[K])
    print(ways[K])

