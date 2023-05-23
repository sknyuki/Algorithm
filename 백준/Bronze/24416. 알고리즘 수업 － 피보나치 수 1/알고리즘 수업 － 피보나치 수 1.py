import sys
input=sys.stdin.readline

def fibo_dfs(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    
    for i in range(3,n+1):
       
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def fibo_DP(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    cnt2=0
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

N=int(input())
print(fibo_dfs(N))
print(fibo_DP(N))
