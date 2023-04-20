import sys
input = sys.stdin.readline
N=int(input())

def sol(A, B):
    cnt = 1
    while True:
        if (A*cnt) % B == 0:
            print(A*cnt)
            break
        else:
            cnt += 1


for i in range(N):
    X, Y = map(int, input().split())
    A=max(X,Y)
    B=min(X,Y)
    sol(A, B)

