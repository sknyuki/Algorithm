import sys
input=sys.stdin.readline

def dfs():
    if len(s)==M:
        print(*s ,sep=" ")
        return
    for i in range(1,N+1):
        s.append(i)
        dfs()
        s.pop()

N,M=map(int,input().split())
s=[]
dfs()