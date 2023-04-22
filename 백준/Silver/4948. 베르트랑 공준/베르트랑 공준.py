import sys
input = sys.stdin.readline


def solution(N):
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True


def find_pn(N, M):
    cnt = 0
    ls = []
    for i in range(N+1, M+1):
        if solution(i):
            cnt += 1
    return cnt


while True:
    N = int(input())
    if N == 0:
        break
    print(find_pn(N, 2*N))
