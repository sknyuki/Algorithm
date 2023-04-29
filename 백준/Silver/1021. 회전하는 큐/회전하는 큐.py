import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
listA = list(i for i in range(1, N+1))
# 스와이퍼로 que 에서 S 까지의 len갯수를 구함
# len(que[0:que.index(S)]) 와 len(que[-1:que.index(S)])+1 중에서 더짧은쪽 실행
# 해당 갯수만큼 que.rotate(-갯수) or que.rotate(+갯수) => cnt+
# popleft()
# 위과정 반복 최종적으로 cnt출력
cnt = 0

num_list = map(int, input().split())
for S in num_list:
    A = len(listA[0:listA.index(S)])
    B = len(listA[-1:listA.index(S):-1])+1
    que = deque(listA)
    if A <= B:
        que.rotate(-A)
        que.popleft()
        cnt += A
        listA = list(que)
    else:
        que.rotate(B)
        que.popleft()
        cnt += B
        listA = list(que)

print(cnt)
