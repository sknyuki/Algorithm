import sys
input = sys.stdin.readline


#pn = list(i for i in range(M, N+1))


def solution(N):
    result = True
    if N == 0 or N == 1:
        result = False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            result = False
            break
    return result


M, N = map(float, input().split())
M, N = int(M), int(N)
for i in range(M, N+1):
    if solution(i):
        print(i)
    if M == N:
        break
