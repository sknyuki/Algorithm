import sys
input = sys.stdin.readline


def backtracking():
    if len(B) == M:
        print(*B, sep=" ")
        return
    for i in A:
        if i not in B:
            B.append(i)
            backtracking()
            B.pop()


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = []

backtracking()
