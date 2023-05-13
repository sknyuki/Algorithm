import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
listA = list(map(int, input().split()))
listA.sort()
for i in range(1, N):
    listA[i] += listA[i-1]
print(sum(listA))
