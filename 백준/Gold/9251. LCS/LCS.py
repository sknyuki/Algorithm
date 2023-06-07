import sys
input = sys.stdin.readline

#    A C A Y K P
#    0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3
# K 0 1 2 3 3 4 4

# 탐색중인 B의 값이 A의 값과 일치하면 dp[y][x]=dp[y-1][x]+1
# else max(dp[y][x-1],dp[y-1][x])

A = list(input().strip())
B = list(input().strip())
LA, LB = len(A)+1, len(B)+1
dp = [[0]*(LA) for _ in range(LB)]

for y in range(1, LB):
    for x in range(1, LA):
        if A[x-1] == B[y-1]:
            dp[y][x] = dp[y-1][x-1]+1
        else:
            dp[y][x] = max(dp[y][x-1], dp[y-1][x])


print(dp[LB-1][LA-1])




