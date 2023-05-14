import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = input().strip()
B=N//2
if A[:B]==A[B:N+1]:
    print("Yes")
else:
    print("No")


