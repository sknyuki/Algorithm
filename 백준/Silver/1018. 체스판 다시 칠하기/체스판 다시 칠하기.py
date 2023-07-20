import sys
from collections import deque
input = sys.stdin.readline

# 스타트가 검은색인 경우와 흰색인 경우
# 다음 색이 같은 색이면 +1인 형식
# list에 K만큼 돌면 저장 해나가는 형식
# 최종적으로 min값을 출력

# [0,0,0,0,0]
# [0,0,1,1,2]
# [0,1,2,3,4]
# [0,1,3,4,5]
# [0,2,4,5,6]


N, M= map(int, input().split())
K=8
board = [list(input().strip()) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
#print(*board, sep="\n")

for i in range(1, N+1):
    for j in range(1, M+1):
        if(i+j) % 2 == 0:
            if board[i-1][j-1] == "B":
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+1
        else:
            if board[i-1][j-1] == "W":
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+1

#print(*dp, sep="\n")
# print("=============")
max_value = -float('inf')
min_value = float('inf')
for r in range(K, N+1):
    for c in range(K, M+1):
        max_value = max(dp[r][c] - dp[r-K][c] - dp[r]
                        [c-K] + dp[r-K][c-K], max_value)
        min_value = min(dp[r][c] - dp[r-K][c] - dp[r]
                        [c-K] + dp[r-K][c-K], min_value)

print(min(min_value, max_value, K*K - min_value, K*K - max_value))