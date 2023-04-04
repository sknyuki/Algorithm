import sys
input=sys.stdin.readline

A,B=map(int,input().split())

listA=[]
for i in range(1,A+1):
   if A%i==0:
       listA.append(i)

try:
    print(listA[B-1])
except:
    print(0)
