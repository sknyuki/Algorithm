import sys
input=sys.stdin.readline
Paper=list([0]*101 for _ in range(101))
N=int(input())

for _ in range(N):
     A,B=map(int,input().split())
     for i in range(10):
         for y in range(10):
             Paper[A+i][B+y]=1
             



result=0
for i in Paper:
    result+=sum(i)

print(result)