import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
x = Counter([i for _ in range(N) if len(i:= sys.stdin.readline().strip()) >= M])
print('\n'.join(sorted(sorted(sorted(list(x.keys())),key=len, reverse=True),key=x.get, reverse=True)))