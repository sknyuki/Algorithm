import sys
input=sys.stdin.readline

N=int(input())

n = 2
a = 1
for i in range(N):
    n += a
    a *= 2
print(n**2)