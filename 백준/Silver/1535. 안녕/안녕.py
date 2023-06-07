import sys
input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
Life = 100
dp = [[0]*Life for _ in range(N+1)]

for y in range(1, N+1):
    for x in range(1, Life):
        if x >= A[0][y-1]:
            dp[y][x] = max(dp[y-1][x-A[0][y-1]]+A[1][y-1], dp[y-1][x])
        else:
            dp[y][x] = dp[y-1][x]

print(dp[-1][-1])
