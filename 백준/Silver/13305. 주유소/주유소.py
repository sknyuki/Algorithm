import sys
input=sys.stdin.readline

N=int(input())
D = list(map(int,input().split()))
C = list(map(int,input().split()))
result = 0

c = C[0]
for i in range(N - 1):
    if c > C[i]:
        c = C[i]
    result += c * D[i]

print(result)