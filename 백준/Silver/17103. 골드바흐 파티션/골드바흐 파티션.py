import sys
input = sys.stdin.readline


def make_pnlist(N):
    listA = [True]*(N+1)
    listA[0] = listA[1] = False
    for i in range(2, int(N**0.5)+1):
        if listA[i]:
            for j in range(i*i, N+1, i):
                listA[j] = False

    return listA


N = int(input())
listA = list(int(input()) for _ in range(N))
pnlist = make_pnlist(max(listA))

for i in listA:
    result = 0
    for j in range((i//2)+1):
        if pnlist[j] and pnlist[i-j]:
            result += 1
    print(result)
