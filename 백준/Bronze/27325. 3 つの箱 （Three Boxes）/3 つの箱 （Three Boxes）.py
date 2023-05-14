import sys
from collections import deque
input = sys.stdin.readline
stack = 1
cnt = 0
N = int(input())
S = input().strip()
for i in S:
    if i == "R":
        if stack < 3:
            stack += 1
        if stack == 3:
            cnt += 1
    else:
        if stack > 1:
            stack -= 1
print(cnt)
