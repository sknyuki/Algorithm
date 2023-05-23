import sys
input=sys.stdin.readline

def fibo_dfs(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    
    for i in range(3,n+1):
       
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


N=int(input())
print(fibo_dfs(N))
print(N-2)

