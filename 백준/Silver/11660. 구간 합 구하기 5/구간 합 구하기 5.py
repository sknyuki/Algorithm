import sys
input = sys.stdin.readline

#[0, 0, 0, 0, 0]
#[0, 1, 3, 6, 10]
#[0, 3, 8, 15, 24]
#[0, 6, 15, 27, 42]
#[0, 10, 24, 42, 64]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]


for y in range(1, N+1):
    for x in range(1, N+1):
        dp[y][x] = dp[y-1][x]+dp[y][x-1]+A[y-1][x-1]-dp[y-1][x-1]
#print(*dp, sep="\n")

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(dp[y2][x2]-dp[y2][x1-1]-dp[y1-1][x2]+dp[y1-1][x1-1])
