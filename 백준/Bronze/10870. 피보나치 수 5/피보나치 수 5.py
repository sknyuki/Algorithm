import sys
input = sys.stdin.readline
N=int(input())
listA = []
for i in range(N+1):
    if i < 2:
        listA.append(i)
    else:
        listA.append(listA[i-2]+listA[i-1])

print(listA[N])
