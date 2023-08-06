import sys
input = sys.stdin.readline

N = int(input())
T = 0
i = 1
while T <= N:
    T += i
    i += 1
print(i-2)
