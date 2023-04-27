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
            top = stack.pop()
            print(top)
        else:
            print(-1)
    elif S[0] == "size":
        print(len(stack))
    elif S[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif S[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
