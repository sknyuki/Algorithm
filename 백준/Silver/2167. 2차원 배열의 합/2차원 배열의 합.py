import sys
from collections import deque
input=sys.stdin.readline
# 배열의 크기 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 부분의 개수 입력
K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])