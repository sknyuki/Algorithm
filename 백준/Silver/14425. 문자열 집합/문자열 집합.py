import sys
input = sys.stdin.readline
N, M = map(int, input().split())
listA =set(list(input().strip() for _ in range(N)))
listB = list(input().strip() for _ in range(M))
count = 0
for i in listB:
    if i in listA:
        count += 1
print(count)
