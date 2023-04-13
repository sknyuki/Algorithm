import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listA = sorted(list(map(int, input().split())))

print(listA[-(M)])
