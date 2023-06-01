import sys
input=sys.stdin.readline

N=int(input())
listA=list(map(int,input().split()))
dp=[1]*N


for i in range(1, N):
    for j in range(i):
        if listA[i]>listA[j]:
            dp[i]=max(dp[i],dp[j]+1) 
print(max(dp))
