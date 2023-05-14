import sys
input = sys.stdin.readline
N = int(input())
S = input()
A = []
cnt = 0
while True:
    if cnt == N:
        break
    if S[cnt] == S[cnt+1]:
        A.append(S[cnt].upper())
        A.append(S[cnt].upper())
        cnt += 2
    else:
        A.append(S[cnt])
        cnt += 1


print(*A, sep="")
