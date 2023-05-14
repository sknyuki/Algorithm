import sys
from collections import deque
input = sys.stdin.readline
A=int(input())
B=int(input())

if A<B:
    print(-1)
elif A==B:
    print(0)
else:
    print(1)