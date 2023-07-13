import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  input()
  A, B, C, D = map(int, input().split())
  for _ in range(D):
    if A >= B and A >= C: A -= 1
    elif B >= A and B >= C: B -= 1
    elif C >= A and C >= B: C -= 1
  print(A * B * C)