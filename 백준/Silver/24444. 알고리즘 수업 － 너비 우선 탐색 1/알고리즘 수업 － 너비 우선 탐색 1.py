import sys
from collections import deque
input=sys.stdin.readline


def BFS(N):
    visited[N]=1
    que=deque()
    que.append(N)
    cnt=2
    while que:
        a=que.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i]=cnt
                cnt+=1
                que.append(i)
                
N,M,R=map(int,input().split())

graph=[[] for i in range(N+1)]

for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

visited=[0]*(N+1)


BFS(R)

for i in range(1,len(visited)):
    print(visited[i])