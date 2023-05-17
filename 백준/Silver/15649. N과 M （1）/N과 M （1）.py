import sys
from itertools import permutations
input = sys.stdin.readline

A, B = map(int, input().split())
listA = list(i for i in range(1, A+1))
nCr = list(permutations(listA, B))

for i in nCr:
    print(*i, sep=" ")
