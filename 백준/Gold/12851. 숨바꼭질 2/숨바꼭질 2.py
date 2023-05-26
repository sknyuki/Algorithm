import sys
from collections import deque
input = sys.stdin.readline

# 수빈이의 행동반경
# -> X+1 or X-1 or 2*X (이동 벡터) 이동 할때 전부 1초 소요
# 찾게 되는 최소 cnt 횟수와 그 경우의 수
# dict사용? key가 min인 값의 value를 추출

# 이번 문제의 solition point
# 1.방문처리의 타이밍을 que.popleft()의 이후에 처리해주는 것
# 2. visited에 직접 이동 횟수를 입력하는 것이 아닌 que의 파라미터로 cnt를 추가


def bfs(s, cnt):
    que = deque()
    que.append([s, cnt])
    locate[s] = 1
    while que:
        s, cnt = que.popleft()
        locate[s] = 1
        if s == K and cnt <= abs(K-N):  # 여동생의 위치에 도달하면 dict[이동횟수]+=1
            if cnt not in cnt_dict.keys():
                cnt_dict[cnt] = 1
            else:
                cnt_dict[cnt] += 1

        for sm in (s-1, s+1, s*2):
            if 0 <= sm < Max and not locate[sm]:
                que.append([sm, cnt+1])


N, K = map(int, input().split())
Max = 100001
locate = [0]*Max
cnt_dict = {}

bfs(N, 0)

for key in cnt_dict.keys():
    print(key)
    print(cnt_dict[key])
    exit(0)
