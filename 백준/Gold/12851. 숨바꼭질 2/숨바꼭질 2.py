import sys
from collections import deque
input=sys.stdin.readline


#가지수를 저장하는 방법..

def bfs(N):
    que=deque()
    que.append(N)
    ways[N]=1
    while que:
        a=que.popleft()
        for i in (a+1,a-1,2*a):

            if 0<=i<=100000: 
                if Time[i]==0:
                    Time[i]=Time[a]+1
                    que.append(i)
                    ways[i]+=ways[a]

                elif Time[i]==Time[a]+1:
                    ways[i]+=ways[a]


N,K=map(int,input().split())

#시간과 가지수
Time=[0]*100001
ways=[0]*100001

if N<K:
    bfs(N)
    print(Time[K])
    print(ways[K])
elif N==K:
    print(0)
    print(1)
else:
    print(N-K)
    print(1)
