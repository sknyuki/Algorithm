import sys
input = sys.stdin.readline

# 조건
# i[0]<i+1[0] and i[1]<i+1[1]이어야 한다.
# 회의실 문제와 유사하다 생각하여 같은 방식으로 접근하였지만 회의실과는 달리 각 항마다 모든 항과 대조를 해야해서 시간초과

# solution
# sort로 i[0]의 올림차순으로 정렬후 i[1]을 기준으로 증가하는 가장 긴 부분수열의 수를 찾아준다.
# 위 작업에서 찾은 max(dp)는 i[0]<i+1[0] and i[1]<i+1[1] 조건을 만족하여 이상이 없는것이기에
# N-max(dp)가 해가 된다.

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [1]*N
A.sort()

for i in range(1, N):  # 가장 긴 증가 부분수열
    for j in range(i):
        if A[i][1] > A[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
