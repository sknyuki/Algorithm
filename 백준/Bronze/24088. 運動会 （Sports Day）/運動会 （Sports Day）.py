import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(input().strip())

for i in range(len(A)):
    if A[i] == "R":
        M -= 1
if M == 0:
    print("W")
else:
    print("R")
