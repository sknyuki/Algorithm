import sys
input = sys.stdin.readline
N = int(input())
setA = set()

for i in range(N):
    A, B = map(str, input().strip().split())
    if A == "ChongChong" or B == "ChongChong":
        setA.add(A)
        setA.add(B)
    if A in setA or B in setA:
        setA.add(A)
        setA.add(B)

print(len(setA))
