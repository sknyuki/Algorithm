import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
sumA = 0
for i in A:
    sumA += i
    if sumA in B:
        sumA = 0
print(sumA)
