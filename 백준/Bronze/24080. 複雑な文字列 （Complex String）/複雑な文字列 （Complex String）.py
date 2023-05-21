import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
listA=set(input().strip())

if len(listA)>=3:
    print("Yes")
else:
    print("No")


