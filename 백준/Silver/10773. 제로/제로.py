import sys
input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    S = int(input())
    if S == 0:
        stack.pop()
    else:
        stack.append(S)
print(sum(stack))
