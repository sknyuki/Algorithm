import sys
input = sys.stdin.readline

N=int(input())
S=input().strip()

for i in range(1,N):
    if S[i]=="J":
        print(S[i-1])