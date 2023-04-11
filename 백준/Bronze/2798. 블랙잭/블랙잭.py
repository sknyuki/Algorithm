import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
listA = list(map(int, input().split()))
com = combinations(listA, 3)
result = 0


for i in com:
    if sum(i) > M:
        pass
    else:
        if result < sum(i):
            result = sum(i)


print(result)
