import sys
input=sys.stdin.readline



C,N=map(int,input().split())
A=[[0,0]]+[list(map(int,input().split())) for _ in range(N)]
dp=[[10000001]*(C+1) for _ in range(N+1)]


for y in range(1,N+1):
    benefit=A[y][1]
    cost=A[y][0]
    for x in range(1,C+1):
        dp[y][x]=dp[y-1][x]
        k=0
        while True:
            if x-(k*benefit)<=0:
                dp[y][x]=min(dp[y][x],k*cost)
                break
            else:
                dp[y][x]=min(dp[y][x],dp[y-1][x-k*benefit]+k*cost)
            k+=1
        
print(dp[-1][-1])