import sys
input = sys.stdin.readline

#     0  1  2  3  4  5  6  7
#     0  0  0  0  0  0  0  0
# 6/13 0  0  0  0  0  0  13 13
# 4/8  0  0  0  0  8  8  13 13
# 3/6  0  0  0  6  8  8  13 14
# 5/12 0  0  0  6  8  12 13 14
# dp[y][x]=dp[y-1][x-A[y-1][0]]+A[y-1][1]

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]


for y in range(1, N+1):
    for x in range(1, K+1):
        if x >= A[y-1][0]:  # 들어 갈 수 있을때
            dp[y][x] = max(dp[y-1][x-A[y-1][0]]+A[y-1][1],
                           dp[y-1][x])  # 원래 가치+ 새로운 가치
        else:  # 안 들어 갈때
            dp[y][x] = dp[y-1][x]

print(dp[-1][-1])
#print(*dp, sep="\n")
