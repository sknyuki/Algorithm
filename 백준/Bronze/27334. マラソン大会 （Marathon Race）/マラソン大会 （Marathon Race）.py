import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int, input().split()))

for i in listA:
    cnt = 1
    for j in listA:
        if i != j and i > j:
            cnt += 1
    print(cnt)
