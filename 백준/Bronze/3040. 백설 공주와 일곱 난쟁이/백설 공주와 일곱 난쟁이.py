from itertools import combinations
import sys
input = sys.stdin.readline

numlist = [ int(input()) for _ in range(9)]

# 9개 중 7개를 뽑을 조합
case = list(combinations(numlist, 7))

# 합이 100이 되면
for i in case:
    if sum(i) == 100:
        for j in i:
            print(j)