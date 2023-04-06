import sys
input = sys.stdin.readline
A, B = int(input()), int(input())
listA = [0]*(B+1)
for i in range(A, B+1):
    temp = 0
    for y in range(2, i+1):
        if i % y == 0:
            temp += 1
    if temp == 1:
        listA[i] = i

X = [i for i in listA if i != 0]

if len(X) > 0:
    print(sum(X))
    print(min(X))
else:
    print(-1)
