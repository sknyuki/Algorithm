import sys
input = sys.stdin.readline
N = int(input())
listA = []
for i in range(N):
    A, B = map(int, input().split())
    listA.append([A, B])

listA.sort(key=lambda X: (X[1], X[0]))

temp = listA[0][1]
cnt = 1
for i in range(1,N):
    if listA[i][0] >= temp:
        cnt += 1
        temp = listA[i][1]
        

print(cnt)
