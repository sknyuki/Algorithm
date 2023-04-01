import sys
input=sys.stdin.readline

N=input().strip()

if N.count(N[0])==len(N):
    print(-1)
elif N==N[::-1]:
    print(len(N)-1)
else:
    print(len(N))