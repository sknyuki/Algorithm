import sys
input = sys.stdin.readline


while True:
    N, M = list(map(int, input().split()))
    if N > M:
        print("Yes")
    elif N == M == 0:
        break
    else:
        print("No")
