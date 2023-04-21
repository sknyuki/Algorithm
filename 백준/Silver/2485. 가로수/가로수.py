import sys
input = sys.stdin.readline


def GCDF(x, y):
    if y == 0:
        return x
    else:
        return GCDF(y, x % y)


N = int(input())
listA = list(int(input()) for _ in range(N))

TD = max(listA)-min(listA)

Dlist = []

for i in range(1, len(listA)):
    Dlist.append(listA[i]-listA[i-1])

# print(min(Dlist))
setDlist = list(set(Dlist))

GCD = setDlist[0]
for i in range(1, len(setDlist)):
    GCD = GCDF(GCD, setDlist[i])

count = TD//GCD

print(count-(len(listA)-1))
