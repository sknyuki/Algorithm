import sys
input = sys.stdin.readline


N = int(input())
M = 2
while N != 1:
    if N % M == 0:
        N = N//M
        print(M)
    else:
        M += 1
