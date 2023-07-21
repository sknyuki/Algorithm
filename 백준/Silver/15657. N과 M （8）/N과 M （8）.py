import sys
input = sys.stdin.readline


def backtracking(temp):
    if len(B) == M:
        print(*B, sep=" ")
        return
    for i in range(temp, N):
        B.append(A[i])
        backtracking(i)
        B.pop()


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = []


backtracking(0)
