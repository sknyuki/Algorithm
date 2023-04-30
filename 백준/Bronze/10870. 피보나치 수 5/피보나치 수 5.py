import sys
input = sys.stdin.readline


def fibo(N):
    if N < 2:
        return N
    else:
        return(fibo(N-2)+fibo(N-1))


print(fibo(int(input())))
