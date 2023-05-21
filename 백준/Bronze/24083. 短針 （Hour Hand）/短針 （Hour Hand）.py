import sys
input = sys.stdin.readline

N=int(input())
M=int(input())
if (N+M)%12==0:
    print(12)
else:
    print((N+M)%12)

