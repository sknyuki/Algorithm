import sys
import math
input = sys.stdin.readline


listA = list(int(input()) for _ in range(3))
M = str(math.prod(listA))

for i in range(10):
    print(M.count(str(i)))
