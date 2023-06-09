import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
m = (A[0]+A[-1])/2

for i in range(N):
    if A[i] <= m:
        print(A[-1]-A[i])
    else:
        print(A[i]-A[0])
