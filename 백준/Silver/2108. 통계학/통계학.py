import sys
import statistics
input = sys.stdin.readline
N = int(input())
listA = list(int(input()) for i in range(N))
listA.sort()
lenA = len(listA)
dictA = {}
listdict = [[0 for _ in range(2)] for _ in range(lenA)]


print(round(sum(listA)/N))
print(listA[(lenA//2)])

for i in listA:
    if i not in dictA.keys():
        dictA[i] = 1
    else:
        dictA[i] += 1

cnt = 0
for i, j in dictA.items():
    listdict[cnt][0] = i
    listdict[cnt][1] = j
    cnt += 1

sortLD = sorted(listdict, key=lambda X: -X[1])

if len(sortLD) != 1 and sortLD[0][1] == sortLD[1][1]:
    print(sortLD[1][0])
else:
    print(sortLD[0][0])

print(max(listA)-min(listA))
