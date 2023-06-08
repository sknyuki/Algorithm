import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
      for money in range(M+1):
          if money >= coin:
              dp[money] += dp[money-coin]
    print(dp[-1])