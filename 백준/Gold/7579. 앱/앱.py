import sys
input = sys.stdin.readline
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
tc = sum(cost)
dp = [[0]*(tc+1) for _ in range(N+1)]
result = 10000001

for y in range(1, N+1):
    for x in range(1, tc+1):
        if x < cost[y-1]:  # 값이 안들어가면
            dp[y][x] = dp[y-1][x]  # 이전 항 호출
        else:  # max(새로운 값,이전 항)
            dp[y][x] = max(memory[y-1]+dp[y-1][x-cost[y-1]], dp[y-1][x])

        # 구한 값이 M보다 큰지 확인
        if dp[y][x] >= M:
            result = min(x, result)

print(result)