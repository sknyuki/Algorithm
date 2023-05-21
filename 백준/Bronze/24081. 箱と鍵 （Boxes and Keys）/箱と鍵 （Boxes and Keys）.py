import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
listA=list(map(int,input().split()))
listB=list(set(map(int,input().split())))

cnt=0

for j in listA:
    if j in listB:
        cnt+=1
print(cnt)

