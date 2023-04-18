import sys
input = sys.stdin.readline
N, M = map(int, input().split())

poke = list(input().strip() for _ in range(N))
poke_num = {poke[i]: i for i in range(len(poke))}

poke_id = {i: poke[i] for i in range(len(poke))}

for i in range(M):
    A = input().strip()
    if A.isdigit():
        print(poke_id[int(A)-1])

    else:
        print(poke_num[A]+1)
