import sys
input = sys.stdin.readline
N = int(input())
setA = set()
cnt = 0
for i in range(N):
    A = input().strip()
    if A == "ENTER":
        cnt += len(setA)
        setA = set()
    else:
        setA.add(A)
cnt += len(setA)
print(cnt)
