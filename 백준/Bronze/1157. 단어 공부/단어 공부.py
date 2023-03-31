import sys
input = sys.stdin.readline

N = input().strip().upper()
SetN = list(set(N))
Serch = []


for i in SetN:
    Serch.append(N.count(i))

if Serch.count(max(Serch)) >= 2:
    print("?")
else:
    print(SetN[Serch.index(max(Serch))])
