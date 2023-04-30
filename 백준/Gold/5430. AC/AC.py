import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

for i in range(N):
    order = input().strip()
    Z = int(input())
    que = deque(input().strip("\n""[""]").split(","))
    if Z < order.count("D"):
        print("error")
    else:
        R = 0  # Reverse token
        for j in order:
            if j == "D":
                if R % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
            else:
                R += 1
        if R % 2 == 0:
            print("[", end="")
            print(*que, sep=",", end="")
            print("]")
        else:
            que.reverse()
            print("[", end="")
            print(*que, sep=",", end="")
            print("]")
