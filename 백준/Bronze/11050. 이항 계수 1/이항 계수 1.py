import sys
import itertools
input = sys.stdin.readline
N, M = map(int, input().split())
listA = list(i for i in range(N))
ncr = itertools.combinations(listA, M)
print(len(list(ncr)))
