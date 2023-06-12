import sys
input = sys.stdin.readline


N = input().strip()

if N == "0":
    print(1)
    exit(0)

if len(N) == 1:
    N = "0"+N

cnt = 0
result = "00"
A, B = int(N[0]), int(N[1])
while result != N:
    C = str(A+B)[-1]
    result = str(B)+C
    A, B = int(result[0]), int(result[1])
    cnt += 1
print(cnt)
