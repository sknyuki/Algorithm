import sys
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
    S = input().strip().split()
    if S[0] == "push":
        stack.append(S[1])
    elif S[0] == "pop":
        if stack:
            print(stack[0])
            stack.remove(stack[0])
        else:
            print(-1)
    elif S[0] == "size":
        print(len(stack))
    elif S[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif S[0] == "front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif S[0] == "back":
        if stack:
            print(stack[-1])
        else:
            print(-1)