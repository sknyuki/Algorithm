import sys
from collections import deque
input = sys.stdin.readline
stack = 1
cnt = 0
N = int(input())
S = input().strip()
for i in range(len(S)):
    if S[i] == "R":
        stack += 1
        if stack > 3:
            stack = 3
        if stack == 3:
            cnt += 1
    else:
        stack -= 1
        if stack < 1:
            stack = 1
print(cnt)
