import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(len(A[i])):
        A[i][j] = max(A[i+1][j], A[i+1][j+1])+A[i][j]
print(A[0][0])
