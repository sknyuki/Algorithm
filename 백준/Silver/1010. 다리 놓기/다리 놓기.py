import sys
input = sys.stdin.readline

def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

N=int(input())
for _ in range(N):
    M, N = map(int, input().split())
    print(factorial(N)//(factorial(M)*factorial(N-M)))