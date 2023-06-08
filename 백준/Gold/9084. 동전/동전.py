import sys
input=sys.stdin.readline


#   |0 1 2 3 4 5 6 7 8
# 0 |0 0 0 0 0 0 0 0 0
# 2 |1 0 1 0 1 0 1 0 1
# 4 |1 0 1 0 2 0 2 0 3
# 6 |1 0 1 0 2 0 3 0 3
# 값이 안 들어 갈 때 dp[y-1][x]
# 값이 들어 갈 때 dp[y][x-C[y-1]]+dp[y-1][x]

T=int(input())
for _ in range(T):
    N=int(input())
    C=list(map(int,input().split()))
    M=int(input())
    dp=[[0]*(M+1) for _ in range(N+1)]

    for i in range(1,N+1): #초기 설정: dp그래프의 모든 0번째 값은 1
        dp[i][0]=1

    for y in range(1,N+1):
        for x in range(1,M+1):
            if x<C[y-1]: #값이 안 들어갈 때 
                dp[y][x]=dp[y-1][x]
            else: #값이 들어 갈 때
                dp[y][x]=dp[y][x-C[y-1]]+dp[y-1][x]

    print(dp[-1][-1])
