import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

A = [0]*91


A[0], A[1], A[2] = 0, 1, 1
if N > 2:
    for i in range(3, N+1):
        A[i] = A[i-2]+A[i-1]

print(A[N])
