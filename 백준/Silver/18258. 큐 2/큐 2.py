import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    S = input().strip().split()
    if S[0] == "push":
        queue .append(S[1])
    elif S[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif S[0] == "size":
        print(len(queue))
    elif S[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif S[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif S[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
