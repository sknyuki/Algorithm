import sys
from collections import deque
input = sys.stdin.readline

N = list(map(int, input().split()))
N.sort()
print(N[1])
