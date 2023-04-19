import sys
input = sys.stdin.readline
N = int(input())


def sol(A, B):
    cnt = 1
    while True:
        if (A*cnt) % B == 0:
            print(A*cnt)
            break
        else:
            cnt += 1


for i in range(N):
    A, B = map(int, input().split())
    if A > B:
        sol(A, B)
    else:
        sol(B, A)
