import sys
input = sys.stdin.readline

# 계단문제와 유사

# 아래 3케이스중 MAX치를 선택 하며 DP에 담으며 진행
# 1)2잔 연속으로 마시는 경우                                    ->(DP[i-3]+listA[i-1]+list[i])
# 2)1잔 마시고 도약하여 다음꺼를 마시는 경우                       ->(DP[i-2]+listA[i])
# 3)도약을 위한것이 아닌 그냥 마시는 경우를 건너 뛴 경우 (예외 조건)  ->(DP[i-1])

# 계단 문제와의 차이점(예외 조건)
# 여러번 안 마시고 건너 뛸 수도 있다->계단은 연속성이 있어야하나 이번 문제는 아니다.

N = int(input())
listA = [int(input()) for _ in range(N)]

DP = [0]*N
DP[0] = listA[0]
if N > 1:
    DP[1] = listA[0]+listA[1]
if N > 2:
    DP[2] = max(listA[0]+listA[2], listA[1]+listA[2], DP[1])  # DP[1]:예외 조건
if N > 3:
    for i in range(3, N):
        DP[i] = max(DP[i-1], DP[i-3]+listA[i-1]+listA[i], DP[i-2]+listA[i])

print(DP[N-1])


