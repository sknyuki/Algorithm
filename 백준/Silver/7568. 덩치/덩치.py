import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split()))for _ in range(N)]

dictA={}
for i in range(N):
    dictA[i]=1
    for j in range(N):
        if A[i][0]<A[j][0] and A[i][1]<A[j][1]:
            dictA[i]+=1
            

       
print(*dictA.values(), sep=" ")
        