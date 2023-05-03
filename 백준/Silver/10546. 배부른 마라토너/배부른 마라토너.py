import sys
input = sys.stdin.readline

N = int(input())
dictA = {}
listA = list(input().strip() for _ in range((N*2)-1))


for i in listA:
    if i not in dictA.keys():
        dictA[i] = 1
    else:
        dictA[i] += 1


print(*[k for k, v in dictA.items() if v % 2 == 1])
