import sys
from collections import deque
input = sys.stdin.readline

N = input().strip()

for i in range(0, len(N), 10):
    print(N[i:i+10])
