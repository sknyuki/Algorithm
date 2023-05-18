import sys
input=sys.stdin.readline

def dfs():
    if len(s)==M:
        print(*s ,sep=" ")
        return
    for i in range(1,N+1):
       if len(s)==0:
          s.append(i)
          dfs()
          s.pop()
          continue
       if i not in s and i>s[len(s)-1]:
        s.append(i)
        dfs()
        s.pop()

N,M=map(int,input().split())
s=[]
dfs()
