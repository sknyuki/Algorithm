import sys
input = sys.stdin.readline
N, M = map(int, input().split())
listA = set(map(int, input().split()))
listB = set(map(int, input().split()))
print(len(listA-listB)+len(listB-listA))
