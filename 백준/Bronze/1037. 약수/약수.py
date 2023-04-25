import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
print(max(listA)*min(listA))
