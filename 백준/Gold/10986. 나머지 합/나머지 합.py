import sys
from itertools import combinations
input = sys.stdin.readline

# 1 3 6 7 9         3 6 9
#   2 5 6 8         6
#     3 4 6         3 6
#       1 3         3
#         2


N, M = map(int, input().split())
A = list(map(int, input().split()))
answer = 0
S = []  # 합배열
C = [0]*M  # 카운팅
mysum = 0

for i in A:
    mysum += i
    S.append(mysum)
# print(S)

for i in S:
    if i % M == 0:
        answer += 1
    C[i % M] += 1
# print(Sm)

for i in range(M):
    if C[i] > 1:  # 같은 나머지값을 가지는 수가 2개 이상있으면
        answer += (C[i]*(C[i]-1))//2
print(answer)
