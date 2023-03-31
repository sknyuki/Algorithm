import sys
input = sys.stdin.readline

N = input().strip()
N = N.upper()
SetN = list(set(N))
Serch = [0]*len(SetN)


for i in range(len(SetN)):
    for y in N:
        if SetN[i] == y:
            Serch[i] += 1


if Serch.count(max(Serch)) >= 2:
    print("?")
else:
    print(SetN[Serch.index(max(Serch))])
