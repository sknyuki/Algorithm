import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(i+1 for i in range(N))
B = []


for i in range(N):
    A.rotate(-K)
    B.append(A.pop())

print("<", end="")
print(*B, sep=", ", end="")
print(">")
