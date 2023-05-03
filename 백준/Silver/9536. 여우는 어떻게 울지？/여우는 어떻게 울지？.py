import sys
input = sys.stdin.readline
N = int(input())
for j in range(N):
    S = list(input().strip().split())
    fox = []
    others = []
    while True:
        say = list(input().strip().split())
        if "what" in say:
            break
        else:
            others.append(say[2])

    for i in S:
        if i not in others:
            print(i, end=" ")
