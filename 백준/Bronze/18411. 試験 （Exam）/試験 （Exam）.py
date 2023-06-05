import sys
input = sys.stdin.readline


A = sorted(list(map(int, input().split())))
print(A[-1]+A[-2])
