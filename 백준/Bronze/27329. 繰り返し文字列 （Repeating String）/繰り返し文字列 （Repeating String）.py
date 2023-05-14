import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = input().strip()
if A[:N//2]==A[N//2:]:
    print("Yes")
else:
    print("No")


