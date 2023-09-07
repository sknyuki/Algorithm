import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))


A = []
for idx, order in enumerate(numlist, 1):
    A.insert((idx-1) - order, idx)


for i in A:
    print(i, end=" ")