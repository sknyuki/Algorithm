import sys
input = sys.stdin.readline
N = int(input())
listA = list(list(map(int, input().split()))for _ in range(N))


listA.sort(key=lambda X: (X[1], X[0]))

for i in range(len(listA)):
    print(listA[i][0], listA[i][1])
