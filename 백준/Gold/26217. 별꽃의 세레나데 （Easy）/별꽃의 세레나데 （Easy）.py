import sys
input = sys.stdin.readline
N = int(input())
listA = []
for i in range(1, N+1):
    listA.append(N/i)
print(sum(listA))
