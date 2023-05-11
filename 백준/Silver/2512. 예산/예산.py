import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))
M = int(input())
listA.sort()

div = M//len(listA)
for i in range(len(listA)):
    if listA[N-1] < div:
        print(listA[N-1])
        break
    if listA[i] < div:
        M -= listA[i]
        div = M//(len(listA)-(i+1))
    else:
        print(div)
        break
