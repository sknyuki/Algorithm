import sys
import math
input = sys.stdin.readline
N = int(input())

def solution(N):
    reslut = True
    if N == 0 or N == 1:
        reslut = False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            reslut = False
            break
    return reslut


for _ in range(N):
    M = int(input())
    while True:
        if solution(M) == True:
            print(M)
            break
        else:
            M += 1
