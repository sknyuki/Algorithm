import sys
input = sys.stdin.readline
N, M = map(int, input().split())

poke = list(input().strip() for _ in range(N))

for i in range(M):
    A = input().strip()
    try:
        A = int(A)
        print(poke[A-1])

    except:
        print(poke.index(A)+1)
