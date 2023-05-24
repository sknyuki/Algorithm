import sys
input = sys.stdin.readline
# 규칙
# 1,1,1,2,2,3,4,5,7,9 ->10 개 는 주어져있음
# 11->12(3+9)
# s[i-5]+s[i-1]
# 12->16(4+12)
# s[12-5]+s[12-1]
T = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]+[0]*91
list_n = [int(input()) for _ in range(T)]
for i in range(max(list_n)):
    if i > 9:
        dp[i] = dp[i-1]+dp[i-5]
for i in list_n:
    print(dp[i-1])
