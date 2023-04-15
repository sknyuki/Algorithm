import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())



for _ in range(C):
    A = (A % B)*10
print(A // B)
