import sys
from collections import deque
input=sys.stdin.readline

def bfs(n):
    cnt=1
    visited[n]=cnt
    que=deque()
    que.append(n)
    while que:
        a=que.popleft()
        for i in graph[a]:
            if visited[i]==0:
                cnt+=1
                visited[i]=cnt
                que.append(i)

N,M,R=map(int,input().split())
graph=[[] for i in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort(reverse=True)

visited=[0]*(N+1)
bfs(R)

for i in range(1,len(visited)):
    print(visited[i])