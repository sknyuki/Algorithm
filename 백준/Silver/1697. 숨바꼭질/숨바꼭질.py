import sys
from collections import deque
input=sys.stdin.readline


def bfs(N,K):
    que=deque()
    que.append(N)
    while que:
        a=que.popleft()
        if a==K:
            return Time[a]
        for i in (a+1,a-1,2*a):
            if 0<=i<=100000 and Time[i]==0:
                Time[i]=Time[a]+1
                que.append(i)

N,K=map(int,input().split())
Time=[0]*100001
print(bfs(N,K))