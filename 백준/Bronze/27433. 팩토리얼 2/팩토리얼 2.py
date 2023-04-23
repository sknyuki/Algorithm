import sys
input=sys.stdin.readline
N=int(input())
A=1
for i in range(1,N+1):
    A*=i
    
print(A)