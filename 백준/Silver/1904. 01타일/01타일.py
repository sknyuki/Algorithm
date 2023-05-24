import sys
input = sys.stdin.readline
# 규칙 탐색
# 1->1
# 2->2
# 3->3
# 4->5
# 5->8
# 피보나치와 동일할 것으로 예상
N = int(input())
dp = [0]*1000001
dp[0], dp[1] = 1, 2
for i in range(2, N):
    dp[i] = (dp[i-1]+dp[i-2]) % 15746

print(dp[N-1])
