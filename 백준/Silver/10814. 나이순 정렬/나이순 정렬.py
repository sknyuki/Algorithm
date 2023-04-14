import sys
input = sys.stdin.readline
N = int(input())
listA = list(list(map(str, input().strip().split())) for _ in range(N))


listA.sort(key=lambda X: (int(X[0])))


for i in range(len(listA)):
    print(listA[i][0], listA[i][1])
