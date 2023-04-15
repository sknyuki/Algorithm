import sys
input = sys.stdin.readline
N = int(input())
listA = set(map(int, input().split()))

N = int(input())
listB = list(map(int, input().split()))


for i in range(len(listB)):
    if listB[i] in listA:
        print(1, end=" ")
    else:
        print(0, end=' ')
