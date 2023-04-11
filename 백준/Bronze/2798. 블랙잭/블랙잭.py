import sys
input = sys.stdin.readline

N, M = map(int, input().split())
listA = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for x in range(j+1, N):
            if listA[i]+listA[j]+listA[x] <= M:
                if result < listA[i]+listA[j]+listA[x]:
                    result = listA[i]+listA[j]+listA[x]

print(result)
