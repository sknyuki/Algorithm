import sys
from collections import deque
input=sys.stdin.readline

A,B=map(int,input().split())
que=deque()
que.append([A,1])
answer=-1
while que:
    i,cnt=que.popleft()
    if i==B:
        answer=cnt
        break
    if i*2<=B:
        que.append([i*2,cnt+1])
    if int(str(i)+'1')<=B:
        que.append([int(str(i)+'1'),cnt+1])
print(answer)

