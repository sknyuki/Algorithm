import sys
input = sys.stdin.readline

N = int(input())
S = set()
for i in range(N):
    order = list(input().split())
    if order[0] == "add":
        if int(order[1]) not in S:
            S.add(int(order[1]))
    elif order[0] == "remove":
        if int(order[1]) in S:
            S.discard(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if int(order[1]) in S:
            S.discard(int(order[1]))
        else:
            S.add(int(order[1]))
    elif order[0] == "all":
        S = {i+1 for i in range(20)}
    elif order[0] == "empty":
        S = set()

