import sys
input = sys.stdin.readline

#1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# 12->9+3
N = int(input())
A = [int(input()) for _ in range(N)]
dp = [0]*N
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]+[0]*91


for j in range(5, max(A)):
    dp[j] = dp[j-1]+dp[j-5]

for i in A:
    print(dp[i-1])

