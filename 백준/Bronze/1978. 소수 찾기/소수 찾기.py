import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
returnA = 0
for i in listA:
    listB = []
    for y in range(1, i+1):
        if i % y == 0:
            listB.append(y)

    if len(listB) == 2:
        returnA += 1

print(returnA)
