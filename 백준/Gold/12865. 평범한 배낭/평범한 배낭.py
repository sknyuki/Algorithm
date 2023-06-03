import sys
input=sys.stdin.readline

#      1  2  3  4  5  6  7
#3/6   0  0  6  6  6  6  6
#4/8   0  0  6  8  8  8  14 ->max(8+6,6)
#5/12  0  0  6  8  12 12 14
#6/13  0  0  6  8  12 13 14 ->max(A[y][1]+dp[y-1][x-A[y][0]],dp[y-1][x])
#                               A[y][1]=현재 물건가치
#                    dp[y-1][x-A[y][0]]=이전물건중 남은 무게만큼에 할당되는 가치
#                            dp[y-1][x]=이전물건중 지금 무게에 할당되는 가치

N,K=map(int,input().split())
A=[[0,0]]+[list(map(int,input().split()))for _ in range(N)]
dp=list([0]*(K+1) for _ in range(N+1))

for y in range(1,N+1):
    for x in range(1,K+1):
        if A[y][0]>x:           #해당 물건이 더 큰 경우 dp[y-1][x]값 배치
            dp[y][x]=dp[y-1][x]
        else:                   #들어가는 경우
            dp[y][x]=max(A[y][1]+dp[y-1][x-A[y][0]],dp[y-1][x])

print(dp[N][K])
            

