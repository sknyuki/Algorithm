import sys
input = sys.stdin.readline

DP = [0] * 11
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 11):
    DP[i] = sum(DP[i-3:i])

T = int(input())
for _ in range(T):
    print(DP[int(input())])