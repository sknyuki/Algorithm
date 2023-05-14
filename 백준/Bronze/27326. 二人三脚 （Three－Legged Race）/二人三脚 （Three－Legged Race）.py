import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
counting = [0]*(max(listA)+1)
for i in listA:
    counting[i] += 1
print(counting.index(1))
