import sys
input = sys.stdin.readline


def backtracking(temp):
    if len(B) == M:
        print(*B)
        return
    for i in range(temp, N):
        if A[i] not in B:
            B.append(A[i])
            backtracking(i+1)
            B.pop()


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = []

backtracking(0)
