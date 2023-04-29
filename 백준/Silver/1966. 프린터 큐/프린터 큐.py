import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    que=deque(map(int,input().split()))
    check = deque(i for i in range(len(que)))#바인딩용
    target=check[B]
    cnt=0
    while target in check:
        cnt+=1
        check.rotate(-que.index(max(que)))
        que.rotate(-que.index(max(que)))
        que.popleft()
        check.popleft() 
    print(cnt)
    